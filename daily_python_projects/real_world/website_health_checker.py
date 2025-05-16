#Project Description
# Create a command-line tool that monitors the health of a list of websites.
# The app reads a website.txt file where you have listed the websites you want to check. For example:

import requests
import csv
from datetime import datetime

input_file = "websites.txt"

# Check the website
def check_webstie(url):
    """Check the health of a website."""
    try:
        response = requests.get(url,timeout = 5)
        status = "Online" if response.status_code == 200 else "Offline"
        return response.status_code, response.elapsed.total_seconds() * 1000, status
    except requests.exceptions.RequestException:
        return  None, None, "Offline"

def log_result(data):
    """Log results to a CSV file."""
    with open("log.csv",mode="a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)

def main():
    # Initialize log file with headers
    with open("log.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "URL", "Response Time (ms)", "Status Code", "Status"])

    with open(input_file, "r") as file:
        websites = [line.strip() for line in file if line.strip()]

    print(f"Checking {len(websites)} websites...")

    for website in websites:
        status_code, response_time, status = check_webstie(website)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{website} - {status} - {status_code if status_code else 'N/A'}")
        log_result([timestamp, website, response_time or "N/A", status_code or "N/A", status])


if __name__ == "__main__":
    main()



