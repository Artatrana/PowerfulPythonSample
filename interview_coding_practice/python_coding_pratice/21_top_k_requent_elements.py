# 21. Top K Frequent Elements – Find the k most frequent numbers/words.
# * Input: `[1,1,1,2,2,3], k=2` → Output: `[1,2]`
# * Input: `[1], k=1` → Output: `[1]`
# * Input: `[4,4,4,5,5,6], k=1` → Output: `[4]`
#   **Logic:** Count with dict, use heap/quickselect to get top k.
# Logic:
# Step 1: Create a diconary - store the fequency of each number
# Step 2: Sort the dicionary items by value(count) in descending order
# Step 3: Pick Top K
# def topKFrequent(nums, k):
#     frequcy = {}
#     for num in nums:
#         frequcy[num] = frequcy.get(num, 0 ) + 1
#
#     #print(frequcy.items(), type(frequcy.items()), frequcy.keys(), type(frequcy.keys()))
#     sorted_frequency = sorted(frequcy.items(), key = lambda x: x[1], reverse=True)
#     #print(sorted_frequency, type(sorted_frequency))
#
#     return [item[0] for item in sorted_frequency[:k]]
#
# print(topKFrequent([1,1,1,2,2,3],2))
# print(topKFrequent([1],1))
# print(topKFrequent([4,4,4,5,5,6],2))

dict_exam1 = {'a':1, 'b': 2, 'c':3}
dict_exam2 = {'d':5, 'e': 10, 'f':15}

dict_exam1.update(dict_exam2)
print(dict_exam1)
