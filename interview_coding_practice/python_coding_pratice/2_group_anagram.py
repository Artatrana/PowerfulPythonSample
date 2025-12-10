# 2. Anagram Groups– Group words that are anagrams.
# Input: `["eat","tea","tan","ate","nat","bat"]` → Output: `[["eat","tea","ate"],["tan","nat"],["bat"]]`
# Input: `["abc","cab","bac"]` → Output: `[["abc","cab","bac"]]`
# Input: `["a"]` → Output: `[["a"]]`
# Logic:Sort each word (signature). Group words with same sorted signature in a dictionary.
# Key concept: make the letters of the work a key or a identifier - so to do that we have arrange the letter
# in a way that every words made form these letters can be mapped with this key: And we can do that id we sort
# the letter also make them standardize. That mean let convert all letter into small case and sort them.
# Create a dictionary to hold the letter key and word made out of that - the value would be a list
# Loop thought the list of the words
# For each word encounter - convert it to samll case - make a list and sort -
# Next find if the key form on above stem is present in Dicionary
# If the key already there - that means the values as a list would be present, so append the letter to the value list
# If not - add a new key value pair -key as the key crated and value as a list with present word


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


