import streamlit as st
import requests

st.set_page_config(page_title="IP Locator", layout="centered")

st.title("IP Address Locatro")
st.write("Enter an IPv4 address like `8.8.8.8` to get location details.")

ip = st.text_input("Enter IP Address", placeholder="e.g. 8.8.8.8")

def get_location(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    return response.json()

if ip:

    data = get_location(ip)
    if data.get("status") == "success":
        st.subheader("📍 Location Details")
        st.write(f"**Country:** {data['country']}")
        st.write(f"**Region:** {data['regionName']}")
        st.write(f"**City:** {data['city']}")
        st.write(f"**ZIP:** {data['zip']}")
        st.write(f"**ISP:** {data['isp']}")
        st.write(f"**Coordinates:** {data['lat']}, {data['lon']}")
        st.map([{"lat": data["lat"],
            "lon": data["lon"]}])
    else:
        st.error("Could not find data for this IP.")


