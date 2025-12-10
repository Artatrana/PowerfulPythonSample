# 18. Find Missing Number– Find the missing number in range `[0, n]`
# * Input: `[3,0,1]` → Output: `2`
# * Input: `[0,1]` → Output: `2`
# * Input: `[9,6,4,2,3,5,7,0,1]` → Output: `8`
#   **Logic:** XOR trick or sum formula `n*(n+1)/2 - sum(nums)`.

def find_missing_number(lst):
    return int((len(lst) * (len(lst) + 1)/2)) - sum(lst)

# print (find_missing_number([3,0,1]))
# print (find_missing_number([0,1]))
# print (find_missing_number([9,6,4,2,3,5,7,0,1]))

from typing import List


def missing_number(nums: List[int]) -> int:
    n = len(nums)
    result = 0

    # XOR with all indices (0 to n)
    for i in range(n + 1):
        #print (result, i)
        result ^= i
        #print(result)

    # XOR with all numbers in array
    for num in nums:
        print(result, num)
        result ^= num
        print(result)

    return result

#print (missing_number([3,0,1]))
print (missing_number([4,2,3,5,7,0,1]))
