# Question:
# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
# Example:
# Input: nums = [1,1,1], k = 2
# Output: 2
# Explanation: The subarrays [1,1] at positions (0,1) and (1,2) both sum to 2.

def subarray_sum(nums, k):
    count = 0
    prefix_sum = 0
    prefix_map = {0: 1}

    for num in nums:
        prefix_sum += num
        count += prefix_map.get(prefix_sum - k, 0)
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
        print(num, prefix_sum, count, prefix_map)
    return count

print(subarray_sum([1, 1, 2,2,2, 3,6], 6))
# # Basic cases
# assert subarray_sum([1, 1, 1], 2) == 2  # [1,1] at (0,1) and (1,2)
# assert subarray_sum([1, 2, 3], 3) == 2  # [1,2] and [3]
# assert subarray_sum([1], 0) == 0        # No subarray sums to 0
# assert subarray_sum([0, 0, 0, 0, 0], 0) == 15  # All possible subarrays sum to 0
#
# # Edge cases
# assert subarray_sum([-1, -1, 1], 0) == 1  # [-1,-1,1] sums to 0
# assert subarray_sum([3, 4, 7, 2, -3, 1, 4, 2], 7) == 4  # multiple options
#
# # Large single number
# assert subarray_sum([10**6], 10**6) == 1  # itself only
#
# print("All test cases passed!")
