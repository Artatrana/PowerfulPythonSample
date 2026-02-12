# This just a demo code to check distributed processing. This code will use 4 core of our machine and
# compute a test fucntion

import concurrent.futures
import os
import psutil

def square(num):
    pid = os.getpid()
    try:
        core = psutil.Process(pid).cpu_num()
        print(f"Number: {num} | Process ID: {pid} | Running on CPU Core: {core}")
    except AttributeError:
        print(f"Number: {num} | Process ID: {pid} | Could not determine CPU core")
    return num * num

if __name__ == "__main__":
    numbers = list(range(1, 11))

    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(square, numbers))

    print("Squared Results:", results)

