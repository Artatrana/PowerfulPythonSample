# Matching Braces / Valid Parentheses– Check if a string of brackets is balanced.
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



