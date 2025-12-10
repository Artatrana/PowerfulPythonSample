# Question:
# Given a string s, find the length of the longest substring without repeating characters.
# Example:
# Input: "abcabcbb"
# Output: 3 (The answer is "abc")
# Logic:

def longest_subtring(s: str) -> str:
    n = len(s)
    result = ''
    start_position = 0
    if n ==0:
        return ""
    if n == 1:
        return s
    seen = set(s[0])
    for i in range(1,n):
        result_new = s[start_position:i]
        if s[i] in seen:
            if len(result_new) > len(result):
                result = result_new
            while start_position < i:
                start_position += 1
                if s[start_position] == s[i]:
                    break
        else:
            seen.add(s[i])
    return result

print(longest_subtring("ab"))
# assert longest_subtring("abcabcbb")=="abc", "pass"
# assert longest_subtring("")==""
# assert longest_subtring("a")=="a"

# Basic examples
# assert longest_subtring("abcabcbb") == "abc" # "abc"
# assert longest_subtring("bbbbb") == "b"    # "b"
# #assert longest_subtring("pwwkew") == "wke"  # "wke"
# assert longest_subtring("") == ""        # Empty string
#
# # Edge cases
# assert longest_subtring(" ") == " "         # Single space
# assert longest_subtring("au") =="au"       # "au"
# assert longest_subtring("dvdf") == "vdf"    # "vdf"
#
# # Longer with mixed repeats
# assert longest_subtring("abcdeafghij") == 10  # "bcdeafghij"

print("All test cases passed!")
