# 9. String Rotation– Check if one string is a rotation of another.
# Input: `"waterbottle", "erbottlewat"` → Output: `True`
# Input: `"abc", "cab"` → Output: `True`
# Input: `"abc", "acb"` → Output: `False`
# Logic: If `len(s1)==len(s2)` and `s2 in (s1+s1)` → True.

# 1. Rotation means you take some character form front and move it to back (or vice versa).
#     Example:
#         "waterbottle" rotated → "erbottlewat" : You just “cut” at some point and swap halves.
# 2. Trick: if you double the first string( concate it with itself), any valid rotation must appear inside it.
#     "waterbottle" + "waterbottle" → "waterbottlewaterbottle" : Check if "erbottlewat" is a substring of that → yes → it’s a rotation.
# 3. Edge cases: lengths must match, empty strings, etc.

def is_rotation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    if not s1:  # both are empty
        return True
    return s2 in (s1+s1)

# More simple code
def is_rotation2(s1, s2):
    return len(s1) == len(s2) and s2 in (s1 + s1)

print(is_rotation("waterbottle", "erbottlewat"))  # True
print(is_rotation("abcde", "cdeab"))              # True
print(is_rotation("abcde", "abced"))              # False
print(is_rotation("", ""))                        # True


def is_rotation(s1: str, s2: str) -> bool:
    # Quick length check
    if len(s1) != len(s2):
        return False
    if not s1:  # both are empty
        return True

    # Trick: check if s2 exists in s1+s1
    return s2 in (s1 + s1)