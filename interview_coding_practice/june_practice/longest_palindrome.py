### Q. Longest Palindrome
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest
# palindrome that can be built with those letters.
# Note: Letters are case sensitive (e.g. ‘Aa’ is not considered a palindrome).
# Input: "abccccdd"
# Output: 7
# Explanation: One longest palindrome is "dccaccd", length is 7.
#Input: "a"
# Output: 1
from numpy.core.defchararray import center

# Logic/ Approrach
#  - A Palindrome can have paired of character mirrorqed around the center
#  - At most one character can remail unpaired( which sits in the middle if needed)
# Steps: 2
# * Count the frequency of each character.
# * For each character:
#   Add the largest even number ≤ its count to the total length (because pairs contribute to palindrome symmetry).
# * If there is any character with odd count, add +1 to the total length (for a possible center character).




def longestPalindrome(s: str) -> int:
    count = {}
