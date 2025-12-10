# 23. First Unique Character in String – Return the index of the first non-repeating character.
# * Input: `"leetcode"` → Output: `0`
# * Input: `"loveleetcode"` → Output: `2`
# * Input: `"aabb"` → Output: `-1`
#   **Logic:** Count chars, return first index with count=1.

# Logic :
# Step 1: Loop though the letter of the string and create a dictioanry of letter and its occurance
# Step 2: loop through the position and letter of the string with Enumerated
#         - For each letter check the count in the dictionary and if its 1
#         - Return the position of the letter


from collections import Counter
def first_unique_char(s):
    count = Counter(s)

    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i
    return -1

print(first_unique_char("leetcode"))     # 0 ('l')
print(first_unique_char("loveleetcode")) # 2 ('v')
print(first_unique_char("aabb"))         # -1 (none)

def first_unique_char2(s):
    count = {}
    for chr in s:
        count[chr] = count.get(chr, 0) + 1

    for i, chr in enumerate(s):
        if count[chr] ==1:
            return i
    return -1

print(first_unique_char2("leetcode"))     # 0 ('l')
print(first_unique_char2("loveleetcode")) # 2 ('v')
print(first_unique_char2("aabb"))         # -1 (none)


