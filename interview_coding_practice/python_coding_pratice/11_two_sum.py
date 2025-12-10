# 11. Two Sum– Find two numbers that add up to a target.
#  Input: `[2,7,11,15], target=9` → Output: `[0,1]`
#  Input: `[3,2,4], target=6` → Output: `[1,2]`
#  Input: `[3,3], target=6` → Output: `[0,1]`
#  Logic: Use a dictionary to store seen numbers and their indices.

def two_sum(lst, sum):
    seen = {}
    result = []
    for i, num in enumerate(lst):
        target = sum - num
        if target in seen:
            return [seen[target], i]
        else:
            seen[num] = i
    return []  # no solution found
print(two_sum([2,7,11,15],9))
print(two_sum([3,2,4],6))
print(two_sum([3,3],6))


