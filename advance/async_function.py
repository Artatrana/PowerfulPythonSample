# Advantage of an async function in Python
#1. Non-blocking execution:
# Async functions allow your program to perform other task while waiting for I/o operation(e.g. API calls, file reads,
# database queries) to complete, instead of blocking the whole program.
#2. Concurrency with fewer resources: They enable concurrent execution without createing multiple thread process
# reducing memory and CPU overhead.
#3. Scalability: Ideal for high I/O-bound task (Web server, data pipelines) because they handel thousand of
# connections efficiently without the cost of threading
#4: Better responsiveness: Improve user experience in application(e.g. Web apps) by keeping them responsive even
# when handling multiple I/O operations
# In short: Async functions make your code faster and more efficient for I/O-bound tasks by allowing other
# operations to proceed without waiting.
# Here is a clear comparison between CPU-bound and I/O-bound tasks with async:
#
# Aspect	    CPU-bound tasks	                                   I/O-bound tasks
# Definition	Heavy computation tasks needing CPU cycles.	       Tasks that wait for external operations (disk, network, DB).
# Async impact	Little or no benefit. Async won’t speed up pure    Significant benefit. Async avoids blocking while waiting for I/O,
#               computation because it uses a single thread and    allowing other tasks to proceed concurrently.
#               just yields control during waits.
#
# Best approach	Use multiprocessing or multithreading to run in    Use asyncio, async/await, or event loops to handle multiple
#               parallel across CPU cores.	                       I/O operations efficiently in the same thread.
# Example	Image processing, matrix multiplication, data encryption.	API calls, reading files, database queries, web scraping.

#Summary
# CPU-bound: Use multiple processes to utilize multiple cores.
# I/O-bound: Use async functions to improve performance and handle many tasks concurrently without blocking.

# # 1. CPU-bound task example (multiprocessing is effective)
# from multiprocessing import Pool
# import time
#
# from tenacity import retry_unless_exception_type
#
#
# def heavy_computation(x):
#     # Simulate CPU-intensive task
#     total = 0
#     for i in range(10**7):
#         total += i * x
#     return total
#
# if __name__ == "__main__":
#     start = time.time()
#
#     with Pool(4) as p:  # Using 4 processes
#         results = p.map(heavy_computation,[1,2,3,4])
#
#     end = time.time()
#     print("CPU-bound results:", results)
#     print("Time taken:", end - start)
#
#     start = time.time()
#     heavy_computation(1)
#     heavy_computation(2)
#     heavy_computation(3)
#     heavy_computation(4)
#     end = time.time()
#     print("Time taken:", end - start)

# 2. I/O-bound task example (async is effective)
import asyncio
import time

async def fetch_data(x):
    print(f"Fetching data {x}...")
    await asyncio.sleep(2)  # Simulate I/O wait
    print(f"Finished fetching data {x}")
    return x * 10

async def main():
    tasks = [fetch_data(i) for i in range(5)]
    results = await asyncio.gather(*tasks)
    print("I/O-bound results:", results)

start = time.time()
asyncio.run(main())
end = time.time()
print("Time taken:", end - start)

