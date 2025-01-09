# Give an array nums, find the contiguous subarray(containging at least one number)
# which has the largest sum and return its sum.

def maxSubArray(num:list[int]) -> int:

    # define total_sum, max_sum 
    total_sum, max_sum = num[0], num[0]
    for i in num[1:]:
        total_sum = max(total_sum + i, i)
        max_sum = max(max_sum, total_sum )

    return max_sum

print(maxSubArray([4, -1, 2,1]))
print(maxSubArray([-2, 1, -3,4,-1,2,1,-5,4]))

