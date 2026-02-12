# 7. Valid Anagram– Check if two strings are anagrams.
#  Input: `"anagram", "nagaram"` → Output: `True`
#  Input: `"rat", "car"` → Output: `False`
#  Input: `"listen", "silent"` → Output: `True`
#  Logic: Sort both strings or count chars using dictionary.

def is_anagram(s: str, t: str) -> bool:
    # Quick length check
    if len(s) != len(t):
        return False

    char_count = {}

    for chr in s:
        char_count[chr] = char_count.get(chr, 0) + 1

    for chr in t:
        if chr not in char_count:
            return False
        char_count[chr] -=1
        if char_count[chr] <0: # we are not checking >0 because we already checked the length- any mismatch will resulted a negative number count
            return  False

    return True

def is_anagram2(s: str, t: str) -> bool:
    # Quick length check
    if len(s) != len(t):
        return False

    return ''.join(sorted(s)) == ''.join(sorted(t))


# print(is_anagram2("anagram", "nagaram"))
# print(is_anagram2("rat", "car"))
# print(is_anagram2("listen", "silent"))
# print(is_anagram2("an", "n"))
# print(is_anagram2("", "car"))
# print(is_anagram2(" ", ""))
print(is_anagram2("", ""))
print(is_anagram2("  ", "  "))
print(is_anagram2("  ", "   "))