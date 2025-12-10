# 8. Roman to Integer– Convert a Roman numeral string to an integer.
# Input: `"III"` → Output: `3`
# Input: `"IV"` → Output: `4`
# Input: `"MCMXCIV"` → Output: `1994`
# Logic: Map symbols to values. If smaller number before bigger → subtract, else add.
from xml.dom.domreg import well_known_implementations

# Step-by-step layman logic:
# 1. Start from the left of the string
# 2. Look at the current symbol and also peek at the next symbol as well
# 3. if current symbol is smaller than next - >  substract current from next
#    Example: "IX" → I (1) is smaller than X (10), so 10 − 1 = 9.
# 4. Otherwise - just add the value.
#     Example "VI" -> V is 5 and I is 1 so add - 5+ 1 = 6
# 5. Keep repeating until the end of the string
# 6. Add all results - thats the integer values

def roman_to_int(s:str) -> int:
    roman_map = {'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
        }
    i = 0
    total = 0
    while i < len(s):
        #print(i)
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]:
            total += roman_map[s[i+1]] - roman_map[s[i]]
            i += 2
        else:
            total += roman_map[s[i]]
            i += 1
            #print(total)
    return total

# print(roman_to_int("III") )
# print(roman_to_int("IV") )
# print(roman_to_int("MCMXCIV") )
print(roman_to_int('IX'))







