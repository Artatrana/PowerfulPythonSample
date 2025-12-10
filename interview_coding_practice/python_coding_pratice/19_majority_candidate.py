# 19. Majority Element– Find the element that appears more than n/2 times.
# * Input: `[3,2,3]` → Output: `3`
# * Input: `[2,2,1,1,1,2,2]` → Output: `2`
# * Input: `[1]` → Output: `1`
#   **Logic:** Boyer–Moore voting algorithm.

def majority_element(nums):
    count = {}
    n = len(nums)
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] > n /2:
            return num

# print(majority_element([3,2,3]))
# print(majority_element([2,2,1,1,1,2,2]))
# print(majority_element([1]))

def majority_element2(nums):
    count = 0
    element = None

    for num in nums:
        if count == 0:
            element = num
        count += (1 if element == num else -1)

    return element

print(majority_element2([3,2,3]))
print(majority_element([2,2,1,1,1,2,2]))

