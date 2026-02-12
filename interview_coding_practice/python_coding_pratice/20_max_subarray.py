# 20. Max Subarray (Kadane’s Algorithm)– Find the contiguous subarray with maximum sum.
#  Input: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]` → Output: `6`(subarray `[4, -1, 2, 1]`)
# *Input: `[1]` → Output: `1`
# *Input: `[5, 4, -1, 7, 8]` → Output: `23`
# Logic: Track running max ending at each index.

def max_subarray(nums):
    current_sum = nums[0]  # start with first element
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray([1]))
print(max_subarray([5, 4, -1, 7, 8]))
