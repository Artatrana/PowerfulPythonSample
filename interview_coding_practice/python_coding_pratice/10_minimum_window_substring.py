# 10. Minimum Window Substring– Find the smallest substring containing all characters of another string.
# Input: `"ADOBECODEBANC", "ABC"` → Output: `"BANC"`
# Input: `"a", "a"` → Output: `"a"`
# Input: `"a", "aa"` → Output: `""`
# Logic: Use sliding window with character counts. Expand & shrink window to cover target.

# Step 1 - Check if both string are valid, I mean no Null and if so, check if length of target string
#         should not exceed length of source string
# Step 2 - Create a dictionary to store no of characters in the target string
# Step 3 - Add another dictionary currently_have to track how many of each character in the current window
# Step 4 - Use two pointer L and R to slide a window over source
# Step 5 - Expand R until window contains all characters
# Step 6 - Shrink L while still valid to get a smallest window
# Step 7 - Keep track of best window seen

def min_window(source: str, target: str) -> str:

    #Edge cases
    if not source and not target and len(target) > len(source):
        return ""

    # Step 2: Build need dictionary
    need = {}
    for chr in target:
        if chr in need:
            need[chr] += 1
        else:
            need[chr] = 1

    have = {}
    required = len(need)  # number of unique chars to satisfy
    formed = 0  # number of unique chars currently satisfied

    best_len  = float('inf')
    best_start = 0

    L = 0
    for R, ch in enumerate(source):
        # Step 2: include character in window
        if ch in need:
            have[ch] = have.get(ch, 0) + 1
            if have[ch] == need[ch]:
                formed += 1

        # Step 3: shrink window from left
        while formed == required and L <= R:
            window_len = R - L + 1
            best_len = window_len
            best_start = L

            left_char = source[L]
            if left_char in need:
                have[left_char] -= 1
                if have[left_char] < need[left_char]:
                    formed -= 1
            L = L +1

    if best_len == float('inf'):
        return ""
    return source[best_start:best_start + best_len]

# print(min_window("ADOBECODEBANC", "ABC"))  # → "BANC"
# print(min_window("a", "a"))                # → "a"
# print(min_window("a", "aa"))               # → ""
# print(min_window("aaflslflsldkalskaaa", "aaa"))  # → "aaa"

# Logic:
# step 1 : check if source and target string are null and len(target) > len(source) - > Return Null
# step 2 : create dictionary of "need" ( character and count) by traversing through the target string
# step 3 : Create another dictionary "have" to add char and its count by traversing thought the source string
#          store count of character which are there in the need
#          Use two pointer technique
#          Use Left and Right
# Step 4: use R - right to traverse through source string
#     step 5: if we have all the character count from the source. Track the best_length and best_start
#     step 6: Shrink L from left to find out best start for each r.

def min_window2(source: str, target: str) -> str:
    if not source  and not target and len(target) > len(source):
        return ""
    need = {}
    for chr in target:
        need[chr] = need.get(chr, 0) + 1

    required_lenght = len(need)
    formed_lenght = 0
    have = {}
    best_length = float('inf')
    best_start = 0
    L = 0
    for R, chr in enumerate(source):
        if chr in need:
            have[chr] = have.get(chr, 0) + 1

            if need[chr] == have[chr]:
                formed_lenght += 1

        # Let check whether it has the minimum length: say we have 4 char need. But to complete characters requirement.
        # We have came across multiple same character. For example: in sring "ABCD" - we need one "A"
        # But in our need dict - we have 4A till we find all other character. So we have to make sure A left most.
        while required_lenght == formed_lenght and L <= R:
            left_char = source[L]
            best_length = min(best_length, R-L+1)
            best_start = L
            if left_char in need:
                have[left_char] -=1
                if have[left_char] < need[left_char]:
                    formed_lenght -= 1

            L = L+1

    if best_length == float('inf'):
        return ""
    #print(best_start,best_length)
    return source[best_start:best_start+best_length+1]

print(min_window2("ADOBECODEBANC", "ABC"))  # → "BANC"
print(min_window2("a", "a"))                # → "a"
print(min_window2("a", "aa"))               # → ""
print(min_window2("aaflslflsldkalskaaa", "aaa"))  # → "aaa"


















