# 16. Product of Array Except Self– Return array where each element is product of all others.
# * Input: `[1,2,3,4]` → Output: `[24,12,8,6]`
# * Input: `[2,3,4,5]` → Output: `[60,40,30,24]`
# * Input: `[1,1,1,1]` → Output: `[1,1,1,1]`
#   **Logic:** Prefix product × Suffix product.
# Logic:
# Step 1: Create a result list (say res) with all elements set to 1
# Step 2: Prefix Pass (Left to Right)
#         * Keep a variable prefix = 1
#         * Traverse the array from left to right.
#         * For each index i:
#             - Set res[i] = prefix (this holds product of all numbers before i).
#             - Update prefix *= nums[i].
# setp 3: Suffix Pass (Right to Left)
#         * Keep a variable suffix = 1.
#         * Traverse the array from right to left.
#         * For each index i:
#             - Multiply res[i] *= suffix (so now res[i] has product of numbers before i × after i).
#             - Update suffix *= nums[i].
#
# step 4: Return result Now res[i] contains product of all numbers except nums[i].

def product_except_self(nums):
    result = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix * result[i]
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums)-1,-1, -1):
        result[i] = postfix * result[i]
        postfix *= nums[i]

    return result

assert (product_except_self([1,2,3,4])) ==[24,12,8,6]
assert (product_except_self([2,3,4,5])) ==[60,40,30,24]
assert (product_except_self([1,1,1,1])) ==[1,1,1,1]
#print("ALl asserts passed")

def product_except_self2(nums):
    result = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        result[i] *= prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums)-1,-1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result

assert (product_except_self2([1,2,3,4])) ==[24,12,8,6]
assert (product_except_self2([2,3,4,5])) ==[60,40,30,24]
assert (product_except_self2([1,1,1,1])) ==[1,1,1,1]
print("ALl asserts passed")