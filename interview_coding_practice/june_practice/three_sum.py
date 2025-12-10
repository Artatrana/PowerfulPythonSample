#Given an array of integers nums, find all unique triplets (a, b, c) such that:
# a + b + c = 0
def three_sum(nums):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n):
        if i >0 and nums[i] == nums[i-1]:
            continue

        start, end  = i +1 , n-1
        print( i, start, end)
        while start < end:
            if (nums[i] + nums[start] + nums[end]) < 0:
                start +=1
            elif (nums[i] + nums[start] + nums[end]) > 0:
                end -= 1
            else:
                result.append([nums[i], nums[start] , nums[end]])
                while start < end and nums[start] == nums[start+1]:
                    start += 1
                while  start < end and nums[end] == nums[end-1]:
                    end -= 1
                start += 1
                end -= 1


    return result

# assert sorted(three_sum([-1, 0, 1, 2, -1, -4])) == sorted([[-1, -1, 2], [-1, 0, 1]])
# print(" All test cases passed! ")

def three_sum_practice2(array):
    # Sort the array to avoid duplicate
    array.sort()
    result = []
    n = len(array)


    for i in range(n):

        if i < n and array[i] == array[i-1]:
            continue

        start, end = i+1, n - 1
        print(i, start, end)

        while start < end:
            print(i, start, end)
            if array[i] + array[start] + array[end] < 0:
                start += 1
            elif array[i] + array[start] + array[end] > 0:
                end -= 1
            else:
                result.append([array[i],array[start], array[end]])
                # skiping if the item are same
                while start < end and array[start] == array[start+1]:
                    start += 1
                # skipping if the item are same from right
                while start < end  and array[end] == array[end - 1]:
                    end -= 1

                start += 1
                end -= 1

    return result

#rint(three_sum_practice2([-1, 0, 1, 2, -1, -4]))
assert sorted(three_sum_practice2([-1, 0, 1, 2, -1, -4])) == sorted([[-1, -1, 2], [-1, 0, 1]])
print(" All test cases passed! ")






