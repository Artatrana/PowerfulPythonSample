# Bubble Sort
def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(len(arr) - i- 1):
            if arr[j] > arr[j+1]:
                arr[j],  arr[j+1] =  arr[j+1],  arr[j]

arr = [5, 3, 8, 4]
bubble_sort(arr)
#print(arr)

# Merge Two sorted list
def merge_sorted_lists(a,b):
    return sorted(a+b)
# print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))

# Given two string, check if they are anagram
def is_anagram(s1, s2 ):
    return sorted(s1) == sorted(s2)

# print(is_anagram("listen", "silent"))
# print(is_anagram("listen", "ilent"))

# 12. Count Vowels in a String
def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")
#print(count_vowels("helloae"))

# 13. Fibonacci Using Recursion
def fibonacci(n):
    return 1 if n <=1 else fibonacci(n-1) + fibonacci(n-2)

#print(fibonacci(10))

# 14. Sum of Digits of a Number
def sum_digits(nums):
    return sum(int(i) for i in str(nums))

# print(sum_digits(1234))

# 15. Find Unique Elements in a List
def unique_elements(lst):
    return list(set(lst))

# print(unique_elements([1, 2, 2, 3, 4, 4, 5]))

# 16. Check Armstrong Number
def is_armstrong(n):
    return n == sum (int(i) ** len(str(n)) for i in str(n))

# print(is_armstrong(153))
# print(is_armstrong(370))
# print(is_armstrong(371))
# print(is_armstrong(156))

# 17. Generate Random Number Between 1 and 100
import random
#print(random.randint(1,100))

# 18. Check Leap Year
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
# print(is_leap_year(2024))
# print(is_leap_year(2025))

# 20. Reverse Words in a String
def reverse_words (s: str) -> str:
    return " ".join (s.split()[::-1])

#print(reverse_words("hello world"))

# 21. Check if All Elements are Unique
def all_unique(lst):
    return lst == list(set(lst))

print(all_unique([1, 2, 3, 4, 5]))

# 22. Transpose a Matrix
def transpose(matrix):
    for rec in zip(*matrix):
        print (list(rec))
    #return list(map(list,zip(*matrix)))

#print(transpose([[1, 2], [3, 4], [5, 6]]))

# 23. Flatten a Nested List
def flatten(lst):
    return [item for sublist in lst for item in sublist]

# print(flatten([[1, 2], [3, 4], [5, 6]]))

# Flatten nested list multi-level 
def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

nested_list = [1, [2, [3, 4], 5], [6, 7], 8, [9, [10, [11, 12]]]]
flattened_list = flatten(nested_list)
#print("Flattened List:", flattened_list)
        
# 24. Convert Decimal to Binary
def decimal_to_binary(n):
    return bin(n)[2:]
print(decimal_to_binary(10))

# 25. Find Intersection of Two Lists
def intersection(a, b):
    return list(set(a) & set(b))
# print(intersection([1, 2, 3], [2, 3, 4]))

# 26. Find LCM of Two Numbers
import math
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)
# print(lcm(12, 15))

# 26. Find LCM of Two Numbers
def lcm1(a,b):
    # Start with the maximum of the two numbers
    lcm = max(a,b )
    while lcm % a != 0 or lcm % b !=0:
        lcm += max(a, b)
    return lcm
# print(lcm1(12, 15))
# print(lcm1(12, 18))

# 

#38. Transpose a Square Matrix In-Place
def transpose_square(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

matrix = [[1, 2], [3, 4]]
transpose_square(matrix)
print(matrix)    

# 39. Find Longest Word in a Sentence

def longest_word(sentence):
    return max(sentence.split(), key=len)
#print(longest_word("find the longest word"))


# 40. Count Frequency of Each Character
from collections import Counter
def char_frequency(s):
    return dict(Counter(s))
#print(char_frequency("hello"))

def char_frequency1(s):
    result_dict = {}
    for char in s:
       result_dict[s] = result_dict.get(char,0) + 1
    return result_dict
#print(char_frequency("hello"))
