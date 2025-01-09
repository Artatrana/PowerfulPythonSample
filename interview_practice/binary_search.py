# Binary Serach
def binary_search(arr : list[int], x: int) -> int:
    # Assuming array is sorted, elase first sort the array and apply below logic
    
    start, end = 0, len(arr) - 1
    while start < end:
        mid = (start + end ) // 2
        if arr[mid] == x:
            return mid 
        elif x > arr[mid]:
            start = mid + 1
        else:
            end = mid-1
    return -1 

print(binary_search([1, 2, 3, 4, 5,23], 3))
