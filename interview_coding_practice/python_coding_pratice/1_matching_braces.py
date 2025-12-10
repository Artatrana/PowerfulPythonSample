# Matching Braces / Valid Parentheses– Check if a string of brackets is balanced.
# Logic:
# Make a map of closing bracket to opening bracket
# Create a empty list to store the encountered braces - we will store only opening braces
# And if we encounter any Closing braces - we will remove braces from the list as that shoud be matching left brace
# with most recent closing braces
# loop though left to write :
#   if we encounter opening braces - then add it to the input_braces list
#   Else: if we encounter closing braces -
#       - First check if the list is empty: if so return False as there is no matching braces
#       - Else take-out the most recent braces with .pop method and check with mapping.
#              - If that won't match then return False
#  Return True


def matching_braces(s):
    input_braces = []
    braceses_mapping = {']':'[', ')':'(', '}':'{'}
    for char in s:
       if char in braceses_mapping:
           if not input_braces:
               return False
           else:
               if braceses_mapping[char] == input_braces[-1]:
                   input_braces.pop()
               else:
                   return False
       else:
           input_braces.append(char)
    if input_braces:
        return False
    else:
       return True

def is_valid_parentheses(s):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}
    for char in s:
        if char in mapping:
            if not stack and stack.pop()!= mapping[char]:
                return False
        else:
            stack.append(char)
    return not stack

print(matching_braces('[]{}'))
print(matching_braces('(]'))
print(matching_braces('({[]})'))
print(matching_braces(''))
print(matching_braces('('))
print(matching_braces(')'))
print(matching_braces('(('))
print(matching_braces('))'))
print(matching_braces('(((((((())))))))'))



