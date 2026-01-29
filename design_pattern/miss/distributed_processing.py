# Distributed processing: One machine Master gives work to other machines(workers), collect result.
# Core concepts:
    # Task queue → send work
    # Worker processes → do work
    # Result queue → send results back

from multiprocessing import Process, Queue
import  time

def worker(task_queue, result_queue, worker_id):
    while True:
        task = task_queue.get()
        if task is None:
            break # shutdown signal

        print(f"Worker {worker_id} processing {task}")
        time.sleep(1)
        result = task * task

        result_queue.put(worker_id, task, result)

# ----- Master -----
if __name__ == "__main__":
    task_queue = Queue()
    result_queue = Queue()

    # Start worker
    workers = []
    for i in range(2):
        p = Process(target=worker, args=(task_queue, result_queue, i))
        p.start()

        workers.append(p)

    # send tasks
    tasks = [1,2,3,4,5]
    for t in tasks:
        task_queue.put(t)

    # stop workers
    for _ in workers:
        task_queue.put(None)

    # collect results
    for _ in tasks:
        print("Result:", result_queue.get())

    for w in workers:
        w.join()
