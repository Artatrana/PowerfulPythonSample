# 13. Merge Intervals– Merge overlapping intervals.
# Input: [[1,3],[2,6],[8,10],[15,18]] → Output: `[[1,6],[8,10],[15,18]]`
# Input: [[1,4],[4,5]] → Output: `[[1,5]]`
# Input: [[1,10],[2,3],[4,5]] → Output: `[[1,10]]`
# Logic: Sort by start. Merge if overlapping.

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

