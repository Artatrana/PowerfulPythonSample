# 6. String Compression– Compress consecutive characters (e.g., `aaabb → a3b2`)
# logic : imagine you are reading the string left to right like a cashier counting items in a row:
# Step
# 1. Start with the first character in the string.
#   * Keep a counter to track how many times the current character appears consecutively.
#   * Initialize the counter to 1
# 2. Move to the next character and continuing scanning:
# * If the current character is same as the previous one:
#       * Increase the counter
# * If the current character is different:
#       * Append the previous character and its count to the result
#       * Reset the counter to 1 for the new character
# 3. Continue this process until you reach till end of the sting
# 4. After finish the loop:
#    * Append the last character and its count to the result ( since it won't be written inside the loop)
# 5. Return the compressed string


def compress_string(s):
    # Edge Cases
    if not s:
        return ""
    if len(s) == 1:
        return s

    result = ""
    counter = 1 # start counting first character

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            counter += 1
        else:
            result += s[i-1] + str(counter)
            counter = 1

    return result+s[-1]+str(counter)

print(compress_string("aaabbccccd"))  # a3b2c4d1
print(compress_string("abc"))   # a1b1c1




