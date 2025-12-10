# Find the second largest lunber in a list
# logic:
# - Initialize the first and second largest with very minimum value
# - Loop though each element in the list and check if the current number > first
# - If its - update the first with new and second with first number
# - if it between first and second update the second number only

def second_largest(nums):
    first = second = float('-inf')
    for i in nums:
        if i > first:
            first, second = i, first
        elif first > i > second:
            second = i
        #print(i, first, second)
    return second if second != float('-inf') else None

nums = [4, 4, 4, 4, 3]
print(second_largest(nums))  # Output: 7

# Basic test with distinct numbers
assert second_largest([5, 2, 9, 1, 7]) == 7

# Largest and second largest are close together
assert second_largest([1, 2]) == 1

# Multiple elements with duplicates
assert second_largest([4, 4, 4, 4, 3]) == 3

# List in ascending order
assert second_largest([1, 2, 3, 4, 5]) == 4

# List in descending order
assert second_largest([5, 4, 3, 2, 1]) == 4

# Negative numbers
assert second_largest([-10, -20, -30, -40]) == -20

# Mixed positive and negative numbers
assert second_largest([-1, -2, 0, 1]) == 0

# All elements are the same
assert second_largest([7, 7, 7, 7]) is None

# Single element list
assert second_largest([42]) is None

# Empty list
assert second_largest([]) is None
