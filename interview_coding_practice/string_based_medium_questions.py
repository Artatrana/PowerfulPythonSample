# Question 1
from interview_coding_practice.group_anagram import group_anagram


def reverse_word(sentence: str):
    word_lst = sentence.split()
    word_lst = reversed(word_lst)
    reversed_sentence = ' '.join(word_lst)
    return reversed_sentence

def reverse_word1(sentence: str):
    word_lst = sentence.split()
    word_lst.reverse()
    reversed_sentence = ' '.join(word_lst)
    return reversed_sentence


def reverse_word2(sentence: str):
    word_lst = sentence.split()
    re_word_lst = []
    for i in range(len(word_lst)-1,-1,-1):
        re_word_lst.append(word_lst[i])
    reversed_sentence = ' '.join(word_lst)
    return reversed_sentence
#print(reverse_word2("the sky is blue"))

def is_palindrome(s:str):
    # remove spaces and convert ot lower cases
    cleaned = s.replace(" ","").lower()
    # Check if cleaned string equals its reverse
    return cleaned==cleaned[::-1]

# Question - 4
# String Compression
# Input: "aabcccccaaa" → Output: "a2b1c5a3"
def sting_compression(s:str) -> str:

    if not s:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i-1]==s[i]:
            count +=1
        else:
            compressed.append(s[i-1]+str(count))
            count = 1
    # Add the last character and its count
    compressed.append(s[-1]+str(count))

    return ''.join(compressed)

# Question - 6
# Check if Two Strings are Anagrams
# Return True if one string is an anagram of another.
def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    # Step 2: Count characters manually using dictionaries
    count1 = {}
    count2 = {}

    for char in s1:
        count1[char] = count1.get(char, 0)

    for char in s2:
        count2[char] = count2.get(char, 0)

    # Step 3: Compare both dictionaries
    return count1 == count2

# Question - 8
# Group Anagrams
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"] → Group into anagram sets.
def group_anagrams(lst: list):
    group_anagram = {}

    for word in lst:
        sort_word = ''.join(sorted(word))
        if sort_word in group_anagram:
            group_anagram[sort_word].append(word)
        else:
            group_anagram[sort_word] = [word]
    return group_anagram

# Question - 9
# Implement strStr()
# Implement function that returns the index of the first occurrence of one string in another.

def strStr(haystack, needle):
    # Step 1: Edge case
    if needle =="":
        return 0
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1
def find_duplicates(s):
    char_count = {}
    dublicate =[]

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in char_count:
        if char_count[char] > 1:
            dublicate.append(char)
    return dublicate

if __name__=="__main__":
    # print(reverse_word2("the sky is blue"))
    #print(is_palindrome("A man a plan a canal Panama"))  # Output: True
    #print(sting_compression("aaabbcccc"))
    # Example usage
    # print(are_anagrams("listen", "silent"))  # Output: True
    # print(are_anagrams("hello", "world"))  # Output: False
    # input_words = ["eat", "tea", "tan",  "ate", "nat", "bat"]
    # print(group_anagrams(input_words))
    # print(strStr("hello", "ll"))  # Output: 2
    # print(strStr("abcdef", "de"))  # Output: 3
    # print(strStr("abc", "d"))  # Output: -1
    # print(strStr("abc", ""))  # Output: 0

    print(find_duplicates("programming"))  # Output: ['r', 'g', 'm']
    print(find_duplicates("helloo"))  # Output: 2

