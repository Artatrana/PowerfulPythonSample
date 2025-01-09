#  This project fetches real-time earthquake data from the USGS (United States Geological Survey) API
#  and displays the 10 strongest earthquakes from the past week. It provides useful insights into the most powerful earthquakes worldwide.

import requests
import pandas as pd

# USGS Earthquake API URL (past 7 days, all magnitudes)
API_URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

def fetch_earthquake_data():
    """Fetch earthquake data from the USGS API and return a Pandas DataFrame."""
    response = requests.get(API_URL)
    data = response.json()

    # Extract relevant fields
    records = []
    for quake in data["features"]:
        props = quake["properties"]
        records.append([
            props["place"],
            props["mag"],
            pd.to_datetime(props["time"], unit="ms"),
            props["url"]  # USGS Event URL
        ])

    return pd.DataFrame(records, columns=["Location", "Magnitude", "Time", "USGS_Link"])

def display_top_earthquakes(df):
    """Display the 10 strongest earthquakes of the past week."""
    print("nTop 10 Strongest Earthquakes This Week:")
    print(df.nlargest(10, "Magnitude"))

if __name__ == "__main__":
    df = fetch_earthquake_data()
    display_top_earthquakes()
