# 2. Anagram Groups– Group words that are anagrams.
# Input: `["eat","tea","tan","ate","nat","bat"]` → Output: `[["eat","tea","ate"],["tan","nat"],["bat"]]`
# Input: `["abc","cab","bac"]` → Output: `[["abc","cab","bac"]]`
# Input: `["a"]` → Output: `[["a"]]`
#  Logic:** Sort each word (signature). Group words with same sorted signature in a dictionary.

def group_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        key = "".join(sorted(word))
        if key not in anagram_dict:
            anagram_dict[key] = [word]
        else:
            anagram_dict[key].append(word)
    return  anagram_dict

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


