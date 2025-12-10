# Problem - 16: **Find Peak Element
# Question: Find a peak element (greater than neighbors).
# Example:
# Input: [1,2,3,1]
# Output: 2  # Index of peak element 3

def findPeakElement(nums):
    left, right = 0 , len(nums) - 1

    while left < right:
        mid = (left + right) //2
        if nums[mid] > nums[mid+1]:
            right =mid
        else:
            left = mid + 1
    return left

assert findPeakElement([1, 2, 3, 1]) in [2]
assert findPeakElement([1, 2, 1, 3, 5, 6, 4]) in [1, 5]
assert findPeakElement([1]) == 0
assert findPeakElement([2, 1]) == 0
assert findPeakElement([1, 2]) == 1

print(" All tests passed!")