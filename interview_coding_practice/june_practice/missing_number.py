def find_missing_number(nums):
    result = 0
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result ^ len(nums)


print(find_missing_number([0,1,2,3,4,6]))
# print(find_missing_number([0, 1,2,5 ,3]))
# print(find_missing_number([0, 1,2,5,8,3]))

