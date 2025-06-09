import multiprocessing
import time

# def cpu_heavy_task():
#     count = 0
#     for _ in range(10**7):
#         count += 1
#
# start = time.time()
#
# # Run 2 processes
# p1 = multiprocessing.Process(target=cpu_heavy_task)
# p2 = multiprocessing.Process(target=cpu_heavy_task)
#
# p1.start()
# p2.start()
# p1.join()
# p2.join()
#
# end = time.time()
# print(f"Processes took: {end - start:.2f} seconds")

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    for c in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {c}")
        time.sleep(1)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=print_numbers)
    p2 = multiprocessing.Process(target=print_letters)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done with both processes!")