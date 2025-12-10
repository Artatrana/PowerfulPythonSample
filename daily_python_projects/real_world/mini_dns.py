#!/usr/bin/env python3
import socket
import struct
import time
from typing import Tuple, Dict, Any, List

# -----------------------------
# Config
# -----------------------------
LISTEN_ADDR = "0.0.0.0"
#LISTEN_PORT = 5353  # use 53 if running with privileges
LISTEN_PORT = 8053
UPSTREAM_DNS = ("8.8.8.8", 53)  # forwarding server

# Authoritative zone (A records only for demo). Add your own.
# Use FQDNs with trailing dots to avoid ambiguity.
ZONES: Dict[str, Dict[str, Any]] = {
    "example.local.": {
        "A": ["10.0.0.10"],
        "TTL": 60,
    },
    "api.example.local.": {
        "A": ["10.0.0.11"],
        "TTL": 60,
    },
}

# -----------------------------
# DNS helpers: encode/decode names & sections
# -----------------------------

def encode_name(name: str) -> bytes:
    """Encode a domain name like 'www.example.com.' into DNS label format."""
    if not name.endswith("."):
        name += "."
    out = b""
    for label in name.split("."):
        if label == "":
            out += b"\x00"
            break
        if len(label) > 63:
            raise ValueError("Label too long in name: %r" % label)
        out += struct.pack("!B", len(label)) + label.encode("ascii")
    return out

def decode_name(packet: bytes, offset: int) -> Tuple[str, int]:
    """
    Decode a (possibly compressed) DNS name starting at offset.
    Returns (name, next_offset). Handles pointers per RFC 1035 4.1.4.
    """
    labels: List[str] = []
    jumped = False
    original_offset = offset
    # to avoid infinite loops
    seen = 0

    while True:
        if seen > 255:
            raise ValueError("Too many labels/pointer jumps; malformed packet")
        seen += 1

        length = packet[offset]
        # pointer: two high bits 11 -> 0xC0
        if length & 0xC0 == 0xC0:
            if offset + 1 >= len(packet):
                raise ValueError("Truncated pointer")
            ptr = ((length & 0x3F) << 8) | packet[offset + 1]
            if not jumped:
                # only move next_offset forward on first jump
                jump_next_offset = offset + 2
            offset = ptr
            jumped = True
            # continue reading labels from pointer target
            continue
        elif length == 0:
            offset += 1
            break
        else:
            offset += 1
            label = packet[offset:offset + length].decode("ascii")
            labels.append(label)
            offset += length

    name = ".".join(labels) + "."
    return (name, (jump_next_offset if jumped else offset))

def parse_header(packet: bytes) -> Dict[str, Any]:
    """
    Parse DNS header. Returns a dict with fields and an index after header (12).
    """
    if len(packet) < 12:
        raise ValueError("Packet too short for DNS header")
    (ident, flags, qdcount, ancount, nscount, arcount) = struct.unpack("!HHHHHH", packet[:12])

    header = {
        "id": ident,
        "flags": flags,
        "qdcount": qdcount,
        "ancount": ancount,
        "nscount": nscount,
        "arcount": arcount,
        "offset": 12,
    }
    return header

def build_flags(qr=0, opcode=0, aa=0, tc=0, rd=1, ra=0, z=0, rcode=0) -> int:
    """Construct 16-bit flags field."""
    flags = 0
    flags |= (qr & 1) << 15
    flags |= (opcode & 0xF) << 11
    flags |= (aa & 1) << 10
    flags |= (tc & 1) << 9
    flags |= (rd & 1) << 8
    flags |= (ra & 1) << 7
    flags |= (z & 0x7) << 4
    flags |= (rcode & 0xF)
    return flags

def parse_question(packet: bytes, offset: int) -> Tuple[Dict[str, Any], int]:
    """Parse a single question section; returns (question_dict, next_offset)."""
    qname, off2 = decode_name(packet, offset)
    if off2 + 4 > len(packet):
        raise ValueError("Truncated question")
    (qtype, qclass) = struct.unpack("!HH", packet[off2:off2 + 4])
    return (
        {"qname": qname, "qtype": qtype, "qclass": qclass},
        off2 + 4,
    )

def pack_header(h: Dict[str, Any]) -> bytes:
    """Write header dict to bytes."""
    return struct.pack(
        "!HHHHHH",
        h["id"],
        h["flags"],
        h["qdcount"],
        h["ancount"],
        h["nscount"],
        h["arcount"],
    )

def pack_question(qname: str, qtype: int, qclass: int) -> bytes:
    return encode_name(qname) + struct.pack("!HH", qtype, qclass)

def pack_rr(name: str, rtype: int, rclass: int, ttl: int, rdata: bytes) -> bytes:
    """Write a resource record (answer/authority/additional)."""
    return (
        encode_name(name)
        + struct.pack("!HHI", rtype, rclass, ttl)
        + struct.pack("!H", len(rdata))
        + rdata
    )

# -----------------------------
# Minimal record handling (A only)
# -----------------------------

TYPE_A = 1
CLASS_IN = 1

def ip_to_bytes(ip: str) -> bytes:
    return socket.inet_aton(ip)

def find_authoritative_a_records(name: str) -> Tuple[List[str], int]:
    """
    Return (list_of_IPs, ttl) for A records we serve; empty list if none.
    Lookup is case-insensitive; stored names should end with dot.
    """
    key = name.lower()
    if key in ZONES and "A" in ZONES[key]:
        return (ZONES[key]["A"], ZONES[key].get("TTL", 60))
    return ([], 0)

# -----------------------------
# Forwarding
# -----------------------------

def forward_query(query: bytes, client_rd_flag: int) -> bytes:
    """
    Forward the raw query to UPSTREAM_DNS and return upstream's response.
    We don't modify it (ID preserved). We rely on upstream for compression.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(3.0)
        s.sendto(query, UPSTREAM_DNS)
        resp, _ = s.recvfrom(4096)
        # optionally ensure RA set (usually upstream does)
        # leave as-is to keep it simple and transparent.
        return resp

# -----------------------------
# Core request handling
# -----------------------------

def build_authoritative_response(query: bytes) -> bytes:
    """
    Parse query, and if we have an A record for qname, build an authoritative response.
    Otherwise return b"" to signal 'not handled here'.
    """
    hdr = parse_header(query)
    offset = hdr["offset"]
    if hdr["qdcount"] != 1:
        return b""  # handle only single-question queries in this demo

    q, next_off = parse_question(query, offset)
    qname = q["qname"]
    qtype = q["qtype"]
    qclass = q["qclass"]

    if qtype != TYPE_A or qclass != CLASS_IN:
        return b""

    ips, ttl = find_authoritative_a_records(qname)
    if not ips:
        return b""

    # Build response
    rd = (hdr["flags"] >> 8) & 1
    resp_hdr = {
        "id": hdr["id"],
        "flags": build_flags(qr=1, opcode=0, aa=1, tc=0, rd=rd, ra=0, z=0, rcode=0),
        "qdcount": 1,
        "ancount": len(ips),
        "nscount": 0,
        "arcount": 0,
    }

    out = bytearray()
    out += pack_header(resp_hdr)
    out += query[hdr["offset"]:next_off]  # echo original question

    # Answers
    for ip in ips:
        rdata = ip_to_bytes(ip)
        out += pack_rr(qname, TYPE_A, CLASS_IN, ttl, rdata)

    return bytes(out)

def handle_query(data: bytes) -> bytes:
    """
    Try to answer from our zones; if not, forward upstream.
    Also demonstrates parsing compressed packets via decode_name when reading upstream if needed.
    """
    # First, see if we can answer authoritatively.
    auth = build_authoritative_response(data)
    if auth:
        return auth

    # Else, we forward it as-is
    # Extract RD bit from original query so we can decide behavior (optional here)
    hdr = parse_header(data)
    client_rd = (hdr["flags"] >> 8) & 1
    try:
        return forward_query(data, client_rd)
    except socket.timeout:
        # Build SERVFAIL
        servfail = {
            "id": hdr["id"],
            "flags": build_flags(qr=1, rd=client_rd, ra=0, rcode=2),  # SERVFAIL
            "qdcount": hdr["qdcount"],
            "ancount": 0,
            "nscount": 0,
            "arcount": 0,
        }
        out = bytearray()
        out += pack_header(servfail)
        # copy original question section if present
        offset = hdr["offset"]
        for _ in range(hdr["qdcount"]):
            q, offset = parse_question(data, offset)
            out += pack_question(q["qname"], q["qtype"], q["qclass"])
        return bytes(out)

# -----------------------------
# UDP server loop
# -----------------------------

def run_server():
    print(f"[{time.strftime('%X')}] DNS server listening on {LISTEN_ADDR}:{LISTEN_PORT}")
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((LISTEN_ADDR, LISTEN_PORT))
        while True:
            data, addr = sock.recvfrom(4096)
            try:
                resp = handle_query(data)
            except Exception as e:
                # On parse or unexpected error, attempt to return a FORMERR
                try:
                    hdr = parse_header(data)
                    formerr = {
                        "id": hdr["id"],
                        "flags": build_flags(qr=1, rcode=1),  # FORMERR
                        "qdcount": 0,
                        "ancount": 0,
                        "nscount": 0,
                        "arcount": 0,
                    }
                    resp = pack_header(formerr)
                except Exception:
                    # If even header parsing fails, drop it.
                    continue
            sock.sendto(resp, addr)

# -----------------------------
# Entry
# -----------------------------
if __name__ == "__main__":
    run_server()
