import os
import sqlite3
import datetime
from collections import defaultdict
from googleapiclient.discovery import build

# --- SETTINGS ---
BROWSER_HISTORY_PATH = os.path.expanduser(
    "~/Library/Application Support/Google/Chrome/Default/History"
)  # Mac Chrome path
# API_KEY = ""
youtube = build("youtube", "v3", developerKey=API_KEY)


# --- FUNCTIONS ---
def get_today_history():
    conn = sqlite3.connect(BROWSER_HISTORY_PATH)
    cursor = conn.cursor()
    today = datetime.datetime.now().date()
    start_ts = datetime.datetime.combine(today, datetime.time.min).timestamp() * 1000000
    end_ts = datetime.datetime.combine(today, datetime.time.max).timestamp() * 1000000

    cursor.execute("""
        SELECT url FROM urls
        WHERE url LIKE '%youtube.com/watch%'
        AND last_visit_time BETWEEN ? AND ?
    """, (start_ts, end_ts))

    urls = [row[0] for row in cursor.fetchall()]
    conn.close()
    return urls


def extract_video_id(url):
    if "watch?v=" in url:
        return url.split("watch?v=")[1].split("&")[0]
    return None


def get_video_categories(video_ids):
    categories = defaultdict(int)
    if not video_ids:
        return categories

    # Fetch category IDs
    request = youtube.videos().list(
        part="snippet,contentDetails",
        id=",".join(video_ids)
    )
    response = request.execute()

    for item in response.get("items", []):
        category_id = item["snippet"]["categoryId"]
        title = item["snippet"]["title"]
        categories[category_id] += 1

    # Map category IDs to names
    cat_req = youtube.videoCategories().list(part="snippet", regionCode="US")
    cat_resp = cat_req.execute()
    id_to_name = {c["id"]: c["snippet"]["title"] for c in cat_resp["items"]}

    return {id_to_name.get(k, "Other"): v for k, v in categories.items()}


# --- MAIN ---
urls = get_today_history()
video_ids = [extract_video_id(u) for u in urls if extract_video_id(u)]
categories_today = get_video_categories(video_ids)

print(f"📅 YouTube usage for {datetime.date.today()}:")
for cat, count in categories_today.items():
    print(f" - {cat}: {count} videos")
