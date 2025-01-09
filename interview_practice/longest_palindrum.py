# Given a sting, write a function to find out longest palindrum substing
def longest_palindrum(s:str) -> str:
    
    def helper(s, l, r):
        while l >=0  and r < len(s) and s[l] == s[r]:
            l -= 1 
            r += 1
        return s[l+1:r]

    res = ""
    for i in range(len(s)):
        odd = helper(s, i, i)
        even = helper(s, i, i+1)
        res = max( odd, even,res, key=len)

    return res

print(longest_palindrum('babad'))

    
        