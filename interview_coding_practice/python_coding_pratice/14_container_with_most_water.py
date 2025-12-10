# 14. Container With Most Water– Given heights, find max water a container can hold.
# Input: `[1,8,6,2,5,4,8,3,7]` → Output: `49`
# Input: `[1,1]` → Output: `1`
# Input: `[4,3,2,1,4]` → Output: `16`
# Logic: Two pointers, move inward from ends, maximize area.
# Step 1: calculate area by starting at left at 0 and right at last index
# Step 2: Move the pointer to the smaller height, because a taller line might increase the area
# Step 3: Keep track the maximum area
# Step 4: stop when left and right meet

def max_area( heights):
    max_water = 0
    left, right = 0, len(heights) - 1

    while left < right:
        width = right - left
        area = min(heights[left],heights[right]) * width
        max_water = max(max_water, area)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_water

print(max_area([1,8,6,2,5,4,8,3,7]))
print(max_area([1,1]))
print(max_area([4,3,2,1,4]))
#print(max_area([0,1,0,2,1,0,1,3,2,1,2,1]))

