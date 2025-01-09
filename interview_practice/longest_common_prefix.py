# Given a list of sting, write a function to return longest common prefix

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
    
