# 24. Trapping Rain Water – Water storage between bars.
# * Input: `[0,1,0,2,1,0,1,3,2,1,2,1]` → Output: `6`
# * Input: `[4,2,0,3,2,5]` → Output: `9`
# * Input: `[2,0,2]` → Output: `2`
#   Logic: Use two pointers and track max left/right walls.
# Goal: Amount of water trapped between bars.
# Logic: Water trapped at a given index depends on :
#     - the heighest bar on left (left_max)
#     - the highest bar on right (right_max)
#     - Water trapped = min(left_max, right_max) - height[i]
# (only if result is positive, otherwise 0)
from keras.src.losses import hinge


# will solve the problem with dynamic problem skill or pre-processing error
# The crux of the logic is - it can store water at a given point if any of its letf and right side building are greater than it.
# So we need to first find out which is the tallest building from left at the position -

# What it mean - we have to traverse/loop though the list or array from left till This point to find what was the max
# height we have see so far including itself and store in the array

# Similarly we have to find out what was the height building at its right side including itself
# By Looping though or traversing from right till the current position and including itself

# Finally - it can hold water at this point - that minimum of both height subtracting the height of itself.

# step 1: for each index, calculate:
#         - left_max[i]: Tallest bar to the left ( including itself)
#         - right_max[i]: Tallest bar to the right( including itself)
# step 2: Loop the array
#     - For each position
#         water[i] = min(left_max[i], right_max[i]) - height[i]
#
# step 3: total water = sum of water in each index

def trap(height):
    if not height:
        return 0

    n = len(height)

    # let's initiate left and right index array with 0 in all the value
    left_max = [0] * n
    right_max = [0] * n

    # let's find out the tallest bar in each position for left_max
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])

    # let's find out the tallest bar in each position for right side that right_max
    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])

    # step 2: compute water
    trapped = 0
    for i in range(n):
        trapped += min(left_max[i], right_max[i]) - height[i]
    return trapped

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))

