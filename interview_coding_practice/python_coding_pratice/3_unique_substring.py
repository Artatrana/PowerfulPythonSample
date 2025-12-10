# 3. Unique Substring– Find the length of the longest substring without repeating characters.
# Input: `"abcabcbb"` → Output: `3 ("abc")`
# Input: `"bbbbb"` → Output: `1 ("b")`
# Input: `"pwwkew"` → Output: `3 ("wke")`
# Logic: Use a sliding window  set to track seen chars. Move window when repeat found.
# Detail Logic:
# First create a Dictionary seen to store the character you encounter to check if its duplicate
# Also initialize a variable max_length  to keep track of maximum length you see so far
# Alos initialize a variable start to keep starting position of the unique string
# Loop though the word by extracting character and its position with enumerate
#   for each pass of the loop
#       - check if the character is already there in the seen dictionary
#       - If yes, that mean the substring is no more consist of unique letter
#       - change the start to character index of the char plus one
#         - if not : I mean if the char is not present in Seen
#         - add the char to seen with value as Index
#         - Also change Max_legnt as there strill unique ness there index - strart + 1
#   Finally return max_length


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