# Given a list of sting, write a function to return longest common prefix
# Plain logic
# Step - 1 . Check if the list is empty - if so, return empty string
# Step - 2. find the shortest word length in the list.
#       This will be max length of the common prefix of the words
# Step - 3. Initialize
#       lcp = lcp (longest common prefix so far) as an empty string.
#       i = 0 to start checking characters from the beginning.
# Step -4. Start looping for i is less than the shortest word length as we find earlier
#       Get the ith character from the first word
#       Loop through the rest of the words
#           if any word has different character in the same position - stop and return the lcp found so far
#       * If all words have the same character at position i:
#          Add that character to lcp.
#          Move to the next character (i += 1).
# Step -5 .Return the full lcp after checking all positions.
#



def longest_common_prefix(strs: list[str]) -> str:

    if len(strs) == 0:
        return ""
    
    min_length = len(strs[0])
    for i in range(len(strs)):
        min_length = min(min_length, len(strs[i]))

    lcp = ""
    i  = 0

    while i < min_length:
        char = strs[0][i]
        for j in range(1,len(strs)):
            if char != strs[j][i]:
                return lcp 
        lcp +=char
        i +=1
    return lcp

print(longest_common_prefix(['flower', 'flow', 'flight']))
print(longest_common_prefix(['dog', 'racecr', 'car']))
    
