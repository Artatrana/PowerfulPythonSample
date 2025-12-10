# 3. Unique Substring– Find the length of the longest substring without repeating characters.
# Input: `"abcabcbb"` → Output: `3 ("abc")`
# Input: `"bbbbb"` → Output: `1 ("b")`
# Input: `"pwwkew"` → Output: `3 ("wke")`
# Logic: Use a sliding window  set to track seen chars. Move window when repeat found.

def length_of_longest_substring(s):

    char_seen = {}
    max_length = start =0

    for i, char in enumerate(s):
        if char in char_seen and char_seen[char] >= start:
            start = char_seen[char] + 1
        char_seen[char] = i
        max_length = max(max_length, i - start + 1)
    return max_length


print(length_of_longest_substring("abcabcbb")) # 3