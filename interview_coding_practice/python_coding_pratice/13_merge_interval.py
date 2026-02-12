# 13. Merge Intervals– Merge overlapping intervals.
# Input: [[1,3],[2,6],[8,10],[15,18]] → Output: `[[1,6],[8,10],[15,18]]`
# Input: [[1,4],[4,5]] → Output: `[[1,5]]`
# Input: [[1,10],[2,3],[4,5]] → Output: `[[1,10]]`
# Logic: Sort by start. Merge if overlapping.
# Descriptive Logic
# Think of this like a booking time slots on a calendar
# Step
# 1. Sort the interval by start time
#   * This ensures that we always process intervals from left to righ
#   * Once sorted, overlapping intervals will appear next to each other
# 2. Initialize a result list
#   * Add the first interval to the result list
#   * This becomes the "current" interval we try to merge into.
# 3. Iterate though the remaining intervals one by one
#   * Compare the current interval with the last interval in the result list
# 4. Check for overlap
#   * If the start of the current interval is less than or equal to the end of the last interval in the result:
#         * The intervals overlap.
#         * Merge them by updating the end of the last interval to the maximum of both ends.
#   *If they do not overlap:
#       * Add the current interval to the result list as a new interval.
# 5. Continue until all intervals are processed
# 6. Return the result list
#   * It now contains only merged, non-overlapping intervals.

def merge_interval(lst:list):
    lst.sort(key=lambda  x: x[0])
    result_list = []
    for item in lst:
        if not result_list or item[0] > result_list[-1][1]:
            result_list.append(item)
        else:
            result_list[-1][1] = max(result_list[-1][1], item[1])
    return result_list

print(merge_interval([[1,3],[2,6],[8,10],[15,18]]))
print(merge_interval([[1,4],[4,5]]))
print(merge_interval([[1,10],[2,3],[4,5]] ))

