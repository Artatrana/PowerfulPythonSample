# 12. Three Sum– Find triplets in an array that sum to zero.
# * Input: `[-1,0,1,2,-1,-4]` → Output: `[[-1,-1,2],[-1,0,1]]`
# * Input: `[0,0,0]` → Output: `[[0,0,0]]`
# * Input: `[1,2,-2,-1]` → Output: `[]`
#   Logic: Sort array, fix one number, use two pointers for the rest.

# Setp 1 : sort the array
# set 2: Traverse though the array form left to right :
#      step 3: for each iteration of number
#         set Left , right and use two pinter for the rest
#         need to be check if there is consecutive element
#         Also need to check for the same number occur consecutively for left and right


def three_sum(lst_unsorted):
    lst = sorted(lst_unsorted)
    result = []

    for i in range(len(lst)-2):

        if i > 0 and lst[i] == lst[i-1]:
            continue
        left = i + 1
        right = len(lst)-1

        while left < right:
            #print(left, right)
            if lst[i] + lst[left] + lst[right] < 0:
                left += 1
            elif lst[i] + lst[left] + lst[right] > 0:
                right -= 1
            else:
                #print(i, left, right)
                result.append([lst[i], lst[left],lst[right]])
                while left < right and lst[left] == lst[left+1]:
                    left +=1
                while left < right and  lst[right] == lst[right-1]:
                    right -=1
                left += 1
                right -= 1
    return result

print(three_sum([-1,0,1,2,-1,-4]))

