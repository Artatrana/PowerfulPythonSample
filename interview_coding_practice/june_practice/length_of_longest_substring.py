def length_of_longest_substring(s: str)-> str:
    seen = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left +=1

        seen.add(s[right])
        max_length = max(max_length, right-left+1)
    return max_length

# Basic examples
assert length_of_longest_substring("abcabcbb") == 3  # "abc"
assert length_of_longest_substring("bbbbb") == 1     # "b"
assert length_of_longest_substring("pwwkew") == 3    # "wke"
assert length_of_longest_substring("") == 0          # Empty string

# Edge cases
assert length_of_longest_substring(" ") == 1         # Single space
assert length_of_longest_substring("au") == 2        # "au"
assert length_of_longest_substring("dvdf") == 3      # "vdf"

# Longer with mixed repeats
assert length_of_longest_substring("abcdeafghij") == 10  # "bcdeafghij"

print("All test cases passed!")