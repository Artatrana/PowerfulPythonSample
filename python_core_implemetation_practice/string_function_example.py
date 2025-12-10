# capitalize()	Converts the first character to upper case
# print("hello world".capitalize())
# casefold()	Converts string into lower case
# print("HELLO".casefold())
# print("hello".casefold())
# center()	Returns a centered string
# print("hello".center(10, "-"))

# count()	Returns the number of times a specified value occurs in a string
#print("hello".count('l'))

# encode()	Returns an encoded version of the string
#print("hello".encode())

# endswith()	Returns true if the string ends with the specified value
#print("python.py".endswith(".py"))  # True

# expandtabs()	Sets the tab size of the string
#print("H\te\tl\tl\to".expandtabs(4))  # H   e   l   l   o

# find()	Searches the string for a specified value and returns the position of where it was found
#print("hello".find("lo"))  # 2

# format()	Formats specified values in a string
# print("My name is {}".format("Ramesh"))  # My name is Ramesh

# format_map()	Formats specified values from a dictionary in a string
data = {"name": "Ramesh", "age": 40}
# print("Name: {name}, Age: {age}".format_map(data))

# index()	Searches the string for a specified value and returns the position of where it was found
# print("name".index("a"))

# isalnum()	Returns True if all characters in the string are alphanumeric
# print("test@".isalnum())

# isalpha()	Returns True if all characters in the string are in the alphabet
# print("test".isalpha())

# isascii()	Returns True if all characters in the string are ascii characters
# print("test!".isascii())

# isdecimal()	Returns True if all characters in the string are decimals
#print("123q".isdecimal())

# isdigit()	Returns True if all characters in the string are digits
# print("123.23".isdigit())

# isidentifier()	Returns True if the string is an identifier
# print("my_var".isidentifier())

# islower()	Returns True if all characters in the string are lower case
#print("test this".islower())

# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# print("test!@# (".isprintable())

# isspace()	Returns True if all characters in the string are whitespaces
# print(" \t\r\f\v\u00A0".isspace())
# istitle()	Returns True if the string follows the rules of a title
# print("Hello World Then".istitle())  # True

# isupper()	Returns True if all characters in the string are upper case
# join()	Converts the elements of an iterable into a string

# ljust()	Returns a left justified version of the string
# print("hi".ljust(5, "*"))  # hi***
# lower()	Converts a string into lower case

# lstrip()	Returns a left trim version of the string
# print("hi".ljust(5, "*"))  # hi***

# maketrans()	Returns a translation table to be used in translations
#trans = str.maketrans("el","12")
#print("hello world".translate(trans))

# partition()	Returns a tuple where the string is parted into three parts
# print("hello world".partition(" "))

# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# print("hello".rfind("l"))  # 3

# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# print("a\nb\nc".splitlines())  # ['a', 'b', 'c']

# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# print("Hello".swapcase())  # hELLO

# title()	Converts the first character of each word to upper case
# print("hello world".title())  # Hello World

# translate()	Returns a translated string

# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

# print("__len__" in dir(str))
# print(dir(str))

print(dir(object))

print("\n\n")
print(dir(type))