# Problem - 12:** Subarray Sum Equals K
# Question: Count how many continuous subarrays sum to k.
# Input: nums = [1,1,1], k = 2
# Output: 2  # ([1,1] at index 0–1 and index 1–2)

def subarraySum(nums, k):
    running_sum = 0
    running_sum_dict = {0: 1}
    count = 0

    for num in nums:
        running_sum += num
        count += running_sum_dict.get(running_sum - k, 0)
        running_sum_dict[running_sum] = running_sum_dict.get(running_sum, 0) + 1
        print(num, running_sum, count, running_sum)

    return count

print(subarraySum ([1, 2, 3], 3))