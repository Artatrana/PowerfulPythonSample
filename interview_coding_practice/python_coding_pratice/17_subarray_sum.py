# 17. Subarray Sum Equals K– Count subarrays that sum to k.
# Input: [1,1,1], k=2` → Output: `2`
# Input: [1,2,3], k=3` → Output: `2`
# Input: [3,4,7,2,-3,1,4,2], k=7` → Output: `4`
# Logic: Use hashmap to store prefix sums. Count how many previous sums make current sum-k.

# Logic:
# Step 1: Initialize running_sum as 0.
#         - Initialize a dicitonary to store sum and it occurance
# Step 2: For each element in the list of number:
#         - Add the number to running_total
#         - Now decuct the target and check if there is sum already OtherRevInfo
#         - If so - increment the counter
#         - If not add the dictionary

def subarray_sum(nums, k):
        count = 0
        prefix_sum = 0
        frequncy_count = {0:1}
        for num in nums:
                prefix_sum += num

                reminder = prefix_sum - k
                if reminder in frequncy_count:
                        count += frequncy_count[reminder]

                frequncy_count[prefix_sum]=frequncy_count.get(prefix_sum,0 ) + 1
        return count

print(subarray_sum([1,1,1], 2))   # 2
print(subarray_sum([1,2,3], 3))   # 2
print(subarray_sum([3,4,7,2,-3,1,4,2], 7))  # 4


