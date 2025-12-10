import time

# def boil_water():
#     print("Boiling water...")
#     time.sleep(5)  # Waits for 5 seconds
#     print("Water boiled!")
#
# def make_tea():
#     print("Making tea...")
#
# boil_water()  # Waits here
# make_tea()    # Runs only after water boils


import asyncio

async def boil_water():
    print("Boiling water...")
    await asyncio.sleep(5)  # Non-blocking wait for 5 seconds
    print("Water boiled!")

async def make_tea():
    print("Making tea...")

async def main():
    task1 = asyncio.create_task(boil_water())  # Start boiling water
    await make_tea()                           # Make tea while water is boiling
    await task1                                # Wait for water to finish boiling

asyncio.run(main())