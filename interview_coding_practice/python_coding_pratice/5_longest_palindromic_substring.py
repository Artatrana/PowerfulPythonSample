# 5. Longest Palindromic Substring– Find the longest palindrome inside a string.
from fontTools.misc.cython import returns
# Input: `"babad"` → Output: `"bab"` (or `"aba"`)
# Input: `"cbbd"` → Output: `"bb"`
# Input: `"a"` → Output: `"a"`
# Logic: Expand around each character (center) to check palindrome. Keep longest.

# Brute force version : Traverse though string twice - for each position
#     again travers though the each character greater than current
#     and store length if the substring is a palindrome
#     - compare them with already recorded length of palindrome
#     - Keep the maximum
# def longest_palindrome(s):
#     result = ""
#     for i in range(len(s)):
#         for j in range(i, len(s)):
#             sub_string = s[i: j+1]
#             if sub_string == sub_string[::-1] and len(sub_string) >len(result):
#                 result = sub_string
#
#     return result
#
# print(longest_palindrome("babad")) # 'bab' or 'aba'
# print(longest_palindrome("cbbd"))   # bb"
# print(longest_palindrome("a"))  #"a"


def longest_palindrome2(s):
    # Edge case if s is Null return ""
    if not s:
        return ""
    start, end = 0, 0

    def expand_from_center(left, right):
        while left >= 0  and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1  # valid palindrome boundaries

    for i in range(len(s)):
        # expand for the odd palindrome
        l1, r1 = expand_from_center(i, i)

        # expand for the even palindrome
        l2, r2 = expand_from_center(i, i+1)

        if r1 - l1 > end -start:
            start, end = l1, r1

        if r2 - l2 > end -start:
            start, end = l2, r2

    return s[start:end +1]

print(longest_palindrome2("babad")) # 'bab' or 'aba'
# print(longest_palindrome2("cbbd"))   # bb"
# print(longest_palindrome2("a"))  #"a"




