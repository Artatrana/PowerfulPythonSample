# 22. Longest Consecutive Sequence – Find longest consecutive numbers in an unsorted array.
# * Input: `[100,4,200,1,3,2]` → Output: `4 ([1,2,3,4])`
# * Input: `[0,3,7,2,5,8,4,6,0,1]` → Output: `9`
# * Input: `[1,2,0,1]` → Output: `3`
# Logic: Use set, expand streaks.
# Step1 : Create a set form the list - to check or lookup the existance of the number
# Step 2: Loop though the each number in the list:
#         - Check if the number just less the current number present for example if first number is 100.
#           Check for presence of 99.
#         - If not
#             -than starting of the sequence is this number, so let find out what other number of this sequence exist
#             - mean after 100, is there 101 is present, then increment the counter
#             - Find the length of the current sequence and check if its max than already present length
#         - if Present: than skip because this is not the starting of the sequence. The starting of the sequence will come later in the list

def longest_consecutive(nums):
    max_length = 0
    set_nums = set(nums)

    for num in nums:
        if num -1 not in set_nums:
            current = num
            length = 1

            while current + 1 in set_nums:
                current = current + 1
                length +=1

            max_length = max(max_length, length)
    return max_length

print(longest_consecutive([100,4,200,1,3,2]))
print(longest_consecutive([0,3,7,2,5,8,4,6,0,1]))
print(longest_consecutive([1,2,0,1]))