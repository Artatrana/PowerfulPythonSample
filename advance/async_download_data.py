# Objectives:
# Download content of multiple websites at the same time instead of one by one.
# Normally, if you fatch 10 websits synchronously, you wait for each to finish -> slow.
# With async, you fetch them concurrently -> much faster

import asyncio
import aiohttp # async HTTP library

urls = [
    "https://www.python.org",
    "https://www.github.com",
    "https://www.wikipedia.org",
    "https://www.stackoverflow.com"
]

# async function to fetch a single URL
async def fetch(session, url):
    async with session.get(url) as response:
        content = await response.text()
        print(f"{url} fetched, {len(content)} characters")
        return content

# async function to fetch all urls concurrently
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks) # run all fetches concurrently
    return results

# run the async program
asyncio.run(main())


