# 25. Find the second largest number in a list

# input: nums = [4, 4, 4, 4, 3] output: 3
# input: nums = [5, 2, 9, 1, 7] output: 7
# input: nums = print(second_largest([5, 2, 9, 1, 7] )) output: 1

# logic:
# - Initialize the first and second largest with very minimum value
# - Loop though each element in the list and check if the current number > first
# - If its - update the first with new and second with first number
# - if it between first and second update the second number only

def second_largest(lst):
    max, second = 0 , 0
    for num in lst:
        if num > max:
            second = max
            max = num

        elif max > num > second:
            second = num
    return second
print(second_largest([4, 4, 4, 4, 3] ))
print(second_largest([5, 2, 9, 1, 7] ))
print(second_largest([1,2] ))