# Problem - 17: **Product of Array Except Self
# Question: Return array where each element is the product of all other elements.
# Example:
# Input: [1,2,3,4]
# Output: [24,12,8,6]

def productExceptSelf(nums):
    # Find the length of the list
    n = len(nums)

    # define a result list with same number of item as supplied list
    result = [1] * n

    # First initialize a prduct
    prefix =1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # first Pass from left to right of the list items
    suffix = 1
    for i in range(n-1, -1 ,-1):
        result[i] *= suffix
        suffix *= nums[i]
    return result

#print(productExceptSelf([1, 2, 3, 4]))

# Basic, no zero — works perfectly
assert productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert productExceptSelf([2, 3, 4, 5]) == [60, 40, 30, 24]

# Single element (edge case)
assert productExceptSelf([10]) == [1]

# All ones
assert productExceptSelf([1, 1, 1, 1]) == [1, 1, 1, 1]

# Negative numbers
assert productExceptSelf([-1, 2, -3, 4]) == [-24, 12, -8, 6]

# Zeros — this version does NOT handle them properly; so don't expect correct results.
# But we can show what it produces:
assert productExceptSelf([0, 2, 3, 4]) == [24, 0, 0, 0]  # only works correctly for single zero at first position
assert productExceptSelf([1, 0, 3, 4]) == [0, 12, 0, 0]

# Empty array — edge case
assert productExceptSelf([]) == []

print("✅ All tests for prefix-suffix version passed!")

def product_except_self(lst):
    n = len(lst)
    result = [1] * n
    prefix  = 1

    for i in range(n):
        result[i] = prefix
        prefix = prefix * lst[i]

    postfix = 1
    for i in range(n-1, -1, -1):
        result[i] *= postfix
        postfix *= lst[i]
    return  result

#print(product_except_self([1, 2, 3, 4]))

# Basic, no zero — works perfectly
assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
assert product_except_self([2, 3, 4, 5]) == [60, 40, 30, 24]

# Single element (edge case)
assert product_except_self([10]) == [1]

# All ones
assert product_except_self([1, 1, 1, 1]) == [1, 1, 1, 1]

# Negative numbers
assert product_except_self([-1, 2, -3, 4]) == [-24, 12, -8, 6]

# Zeros — this version does NOT handle them properly; so don't expect correct results.
# But we can show what it produces:
assert product_except_self([0, 2, 3, 4]) == [24, 0, 0, 0]  # only works correctly for single zero at first position
assert product_except_self([1, 0, 3, 4]) == [0, 12, 0, 0]

# Empty array — edge case
assert product_except_self([]) == []

print("✅ All tests for prefix-suffix version passed!")


