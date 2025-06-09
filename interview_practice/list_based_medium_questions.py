# Question - 1
# Remove Duplicates from List
# Given a list of integers, return a new list with duplicates removed, preserving order.

def remove_duplicate(lst: list) -> list:
    seen = set()
    result_list = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result_list.append(num)

    return result_list

data_lst = [4, 5, 4, 1, 2, 5, 3, 2, 1]
#print(remove_duplicate(data_lst))

# Question - 2
# Find All Pairs with a Given Sum
# Given a list of integers and a target sum, return all unique pairs that sum up to the target.

def find_pairs_with_sum(nums: list[int], target: int) -> list[tuple[int, int]]:
    seen = set()
    output = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            # Store sorted tuple to avoid duplicate pairs like (2,3) and (3,2)
            output.add(tuple(sorted((num, complement))))
        seen.add(num)

    return list(output)

nums = [1, 2, 3, 2, 4, 3]
target = 5
result = find_pairs_with_sum(nums, target)
#print(result)

# Question - 3
# Rotate List
# Rotate a list to the right by k positions.
# Example: [1, 2, 3, 4, 5], k=2 → [4, 5, 1, 2, 3]

def rotate_list(lst: list, k: int) -> list:
    if len(lst) == 0:
        return lst
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

#print(rotate_list([1, 2, 3, 4, 5],2))

# Question - 4
# Flatten a Nested List
# Flatten a list that may contain nested lists.
# Input: [1, [2, [3, 4]], 5] → Output: [1, 2, 3, 4, 5]
def flatten_list(lst: list) -> list:
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

#print(flatten_list([1, [2, [3, 4]], 5]))

# Question - 6
# Partition List by Parity
# Rearrange a list so all even numbers appear before odd numbers.
def partition_by_parity(nums: list) -> list:
    even_lst = [i for i in nums if i %2 ==0]
    odd_lst = [i for i in nums if i % 2 != 0]
    return even_lst + odd_lst

# print(partition_by_parity([3, 1, 2, 4]))  # Output: [2, 4, 3, 1]
# print(partition_by_parity([10, 5, 8, 3, 7]))  # Output: [10, 8, 5, 3, 7]

print(sorted([[1,2], [4,10],[12,2],[34,7]],key=lambda x: x[1]))

# Question - 8
# Product of All Except Self
# For each index in the list, return the product of all other elements.
# Input: [1,2,3,4] → Output: [24,12,8,6]

def product_all_except_self(nums: list) -> list:
    n = len(nums)
    result = [1] * n

    # Left pass
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]

    # right pass
    right_product = 1
    for i in range(n-1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    return result

print(product_all_except_self([1, 2, 3, 4]))





