# Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.
# Example:
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

def merge_intervals(lst: list) -> list:

    if not lst:
        return []
    # Step 1: Sort intervals by start time
    lst.sort(key=lambda x: x[0])

    result = [lst[0]]

    for item in lst[1:]:
        if result[-1][1] >= item[0]:
            result[-1][1] = max(item[1], result[-1][1])
        else:
            result.append(item)
    return result

#print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]) )



# Basic Test cases
assert merge_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
assert merge_intervals([[1,4],[4,5]]) == [[1,5]]
assert merge_intervals([[1,4],[0,4]]) == [[0,4]]

# Edge cases
assert merge_intervals([]) == []
assert merge_intervals([[1,4]]) == [[1,4]]
assert merge_intervals([[1,4],[5,6]]) == [[1,4],[5,6]]

# Unordered input
assert merge_intervals([[6,8],[1,3],[2,4]]) == [[1,4],[6,8]]

#  Fully overlapping intervals
assert merge_intervals([[1,10],[2,3],[4,8]]) == [[1,10]]

#  Nested and overlapping mix
assert merge_intervals([[1,5],[2,3],[4,6],[7,9]]) == [[1,6],[7,9]]

