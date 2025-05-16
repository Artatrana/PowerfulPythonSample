from datetime import datetime, timedelta

# Step 1: Define a dictionary of Indian festivals with their dates (Month-Day format)
festivals = {
    "Diwali": "11-01",
    "Holi": "03-25",
    "Navratri": "10-03",
    "Raksha Bandhan": "08-19",
    "Eid": "04-10",
    "Pongal": "01-14",
}

# Step 2: Get today's date and format it as Month-Day
today = datetime.today().strftime("%m-%d")
print(type(today),today)

# Step 3: Check if today is a festival
if today in festivals.values():
    festival_name = [name for name, date in festivals.items() if date == today][0]
    print(f"🎉 Happy {festival_name}! Enjoy the celebrations! 🎊")
else:
    # Step 4: Find the next upcoming festival
    upcoming_festivals = {name: date for name, date in festivals.items() if date > today}
    print(upcoming_festivals)
    print(upcoming_festivals.get)
    if upcoming_festivals:
        next_festival = min(upcoming_festivals, key=upcoming_festivals.get)
        festival_date = datetime.strptime( upcoming_festivals[next_festival], "%m-%d")
        days_left = (festival_date - datetime.strptime(today, "%m-%d")).days
        print(f"⏳ {next_festival} is in {days_left} day(s). Get ready! 🎆")
    else:
        print("No upcoming festivals for the rest of the year. Stay tuned for next year's celebrations! 🎇")

