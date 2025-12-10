import time
from datetime import datetime
from zoneinfo import ZoneInfo

print("=" * 60)
print("CURRENT UNIX TIMESTAMP (seconds since Jan 1, 1970 )")
print("="* 60)
current_ts = time.time()
print("Epoch time:", current_ts)

print("\n"+ "=" * 60)
print("2. CONVERT TIMESTAMP → LOCAL TIME STRUCT")
print("="* 60)
local_time= time.localtime(current_ts)
print("Local Time Struct:", local_time)

print("\n"+ "=" * 60)
print("3. CONVERT TIMESTAMP → UTC TIME STRUCT")
print("=" * 60)
utc_time = time.gmtime(current_ts)
print("UTC Time Struct:", utc_time)

print("\n" + "=" * 60)
print("4. FORMAT TIME AS STRING (strftime)")
print("=" * 60)
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("Formatted Local Time:", formatted_time)

print("\n" + "=" * 60)
print("5. PARSE STRING → TIME STRUCT (strptime)")
print("=" * 60)
time_string = "2025-12-03 10:30:00"
parsed_time = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
print("Parsed Time Struct:", parsed_time)

print("\n" + "=" * 60)
print("6. SLEEP / DELAY EXECUTION")
print("=" * 60)
print("Sleeping for 2 seconds...")
time.sleep(2)
print("Awake now!")

print("\n" + "=" * 60)
print("7. MEASURE EXECUTION TIME (PERFORMANCE TIMER)")
print("=" * 60)
start = time.perf_counter()

total = 0
for i in range (1_000_000):
      total += i
end = time.perf_counter()
print("Execution time:", end - start, "seconds")

print("\n" + "=" * 60)
print("8. CPU PROCESS TIME (EXCLUDES SLEEP)")
print("=" * 60)
cpu_start = time.process_time()

for i in range (1_000_000):
      total += i
cpu_end = time.process_time()
print("CPU Time Used:", cpu_end - cpu_start, "seconds")

print("\n" + "=" * 60)
print("9. TIME ZONE USING datetime + zoneinfo (RECOMMENDED)")
print("=" * 60)

# Local Time
local_dt = datetime.now()
print("Local time:", local_dt)

# UTC Time
utc_dt = datetime.now(tz=ZoneInfo("UTC"))
print("UTC Time:", utc_dt)

# US Pacific Time
pst_dt = datetime.now(tz=ZoneInfo("America/Los_Angeles"))
print("US Pacific Time:", pst_dt)

# India Time
india_dt = datetime.now(tz=ZoneInfo("Asia/Kolkata"))
print("India Time:", india_dt)


print("\n" + "=" * 60)
print("10. TIME ZONE CONVERSION")
print("=" * 60)
converted = utc_dt.astimezone(ZoneInfo("Asia/Kolkata"))
print("UTC → India Time:", converted)

print("\n" + "=" * 60)
print("11. GET TIME ZONE OFFSET")
print("=" * 60)
offset = india_dt.utcoffset()
print("India UTC Offset:", offset)

print("\n" + "=" * 60)
print("✅ DEMO COMPLETE")
print("=" * 60)


