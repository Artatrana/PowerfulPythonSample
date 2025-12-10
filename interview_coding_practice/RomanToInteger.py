def roman_to_integer(s: str) -> int:
    
    val_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,}

    total = 0 
    curr = 0
    prev = 0

    for i in range(len(s)):
        curr = val_dict[s[i]]
        if curr > prev:
            total += curr - 2 * prev
        else:
            total += curr

        prev = curr 

    return total

#print(roman_to_integer('XLIX') )
# #assert(roman_to_integer('XLIX') == 49, "please check")

assert roman_to_integer('XLIX')  == 49, f"Expected 49, but got differnt value" 

print("Test passed!")
    


