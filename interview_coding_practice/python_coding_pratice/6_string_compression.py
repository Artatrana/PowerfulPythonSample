# 6. String Compression– Compress consecutive characters (e.g., `aaabb → a3b2`)
# logic : imagine you are reading the string left to right like a cahsier counting items in a row:
# 1. Start with the first item(character)
#   * Keep a counter in your hand
# 2. Keep looking at the next item
#  * if its same - increase the counter
#  * if its different -
#     * write down previos item + count
#     * Rest counter = 1 (because new item starts)
# 3. At the end, don’t forget to write the last group!

def compress_string(s):
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




