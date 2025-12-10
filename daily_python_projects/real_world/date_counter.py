# Enter your target date (e.g., 2025-08-11, 11/08/2025, Aug 11, 2025): Aug 11, 2025
# (Optional) Enter a time of day (e.g., 15:30), or press Enter to skip: 14:35
#
# Target: Monday, August 11, 2025 at 14:35
# Weekend: No
# Time remaining: 365 days, 2 hours, 10 minutes
# (If the date has passed this year, counting to next year's occurrence.)

from datetime import datetime
from dateutil import parser

def ask_datetime():
    while True:
        date_str = input("Enter your target date (e.g., 2025-08-11, 11/08/2025, Aug 11, 2025): ").strip()
        time_str = input("(Optional) Enter a time of day (e.g., 15:30), or press Enter to skip: ").strip()
        full = f"{date_str} {time_str}" if time_str else date_str
        try:
            dt = parser.parse(full, dayfirst=False)
            return dt
        except Exception:
            print("Couldn't parse that. Try formats like: 2025-08-11 | 11/08/2025 | Aug 11, 2025 | 11 Aug 2025 15:30")


def next_occurrence(dt: datetime, now: datetime) -> datetime:
    # If the input lacked an explicit year (parser might add current year), we still treat as annual
    target = dt.replace(year=now.year)
    if target <= now:
        target = target.replace(year=now.year + 1)
    return target

def berekdwon(delta):
    days = delta.days
    hours, rem = divmod(delta.seconds, 3600)
    minutes, _ = divmod(rem, 60)
    return days, hours, minutes

now = datetime.now()
dt = ask_datetime()
#target = next_occurrence(dt, now) if dt <= now else dt
target = next_occurrence(dt, now) if dt <= now else dt
delta = target -now
days, hours, minutes = berekdwon(delta)
weekday = target.strftime("%A")
is_weekend = weekday in {"Saturday", "Sunday"}
verbose = target.strftime("%A, %B %d, %Y at %H:%M")
print(f"\nTarget: {verbose}")
print("Weekend:", "Yes" if is_weekend else "No")
print(f"Time remaining: {days} days, {hours} hours, {minutes} minutes")
if dt <= now:
    print("(If the date has passed this year, counting to next year's occurrence.)")

