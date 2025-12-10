# 4. Palindrome Check– Check if a string is a palindrome, ignoring spaces/punctuation.
# Input: `"A man, a plan, a canal: Panama"` → Output: `True`
# Input: `"racecar"` → Output: `True`
# Input: `"hello"` → Output: `False`
#   Logic:
#   Clean string (lowercase, alphanumeric only). Compare string with its reverse.

def is_palindrome(s):

    # Keep only alphanumeric character and convert them to lower case
    cleaned = ''.join(char.lower() for char in s if char.isalpha())

    # Check if cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Example usage
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))