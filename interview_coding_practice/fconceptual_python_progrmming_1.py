# Revers String
def reverse_string(s):
    return s[::-1]

#print(reverse_string("hello"))

# Check if number is Prime
def is_prime(num):
    return all(num %i != 0 for i in range(2,int(num//2)+1))
# print(is_prime(7))
# print(is_prime(0))
# print(is_prime(12.5))
# print(is_prime(12))
# print(is_prime(37))

# Fibonacci Sequence 
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a , end = " ")
        a, b = b, a+b 
# fibonacci(10)

# Factorial 
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

# print(factorial(5))

# Check if supplied string is a palindrome 
def is_palindrome(s):
    return s == s[::-1]

# print(is_palindrome("madam"))
# print(is_palindrome("madami"))

# 6. Find GCD of Two Numbers
import math
def gcd(a,b):
    return math.gcd(a,b)

#print(math.gcd(24, 18))

def gcd1(a,b):
    while b:
        a, b = b, a % b
    return abs(a) # return absolute value to handle negative inputs

print(math.gcd(24, 18)) 
print(math.gcd(15, 35)) 

