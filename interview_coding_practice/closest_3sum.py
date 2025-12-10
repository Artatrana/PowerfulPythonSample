# Givean an array nums of n integers and an integer target, find the three integers
# that the sum is closest to target.

def closest_3sum(nums: list[int], target: int) -> int:
    
    result = sum(nums[:3])
    nums.sort()

    for i in range(len(nums)-2):
        start = 1
        end = len(nums)-1
        while start < end:
            current_sum = nums[i] + nums[start] + nums[end]
            if abs(current_sum - target) < abs(result - target):
                result = current_sum
            if current_sum < target:
                start +=1
            else:
                end -= 1
    return result

print(closest_3sum([-1,2,1,4],1))
        

