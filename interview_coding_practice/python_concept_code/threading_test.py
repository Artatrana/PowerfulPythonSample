# Threading test program. Thread are controled by GIL. Multi threading are most suitable for I/O intensive work
# Even if machine have multi core, Only one python interpreter will run.

import threading
import time

def cpu_heavy_task():
    count = 0
    for _ in range(10**7):
        count += 1

start = time.time()

# Lets run two thread for cpu_heavy_task
thread1 = threading.Thread(target=cpu_heavy_task)
thread2 = threading.Thread(target=cpu_heavy_task)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end = time.time()
print(f"Threads took: {end - start:.2f} seconds")

