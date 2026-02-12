# Matching Braces / Valid Parentheses– Check if a string of brackets is balanced.
# Logic:
# * Create a mapping of closing brackets to their corresponding opening brackets
# * Use a stack ( list) to keep track of opening brackets encountered
# * Iterate through each character in the string
#   * If it is an opening bracket, push it onto the stack
#   * if it is a closing bracket:
#       * if the stack is empty, return False
#       * Pop the last opening bracket from the stack
#       * If it does not match the expected opening bracket, return False
# After processing all the characters, return True only if stack is empty

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



