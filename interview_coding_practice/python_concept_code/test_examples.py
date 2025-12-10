import importlib.util
import keyword
import operator
import math
import pandas as pd

data_dict = dict(key1=100, key2=200, key3=300)
#print(data_dict.__getattribute__('keys'))

# from timeit import timeit
# print(timeit("(1,2,3,4,5,6)",number=10_000_000 ))
# print(timeit("[1,2,3,4,5,6]",number=10_000_000 ))

# a, b = 1, 1
# print(id(a), id(b))
#
# a, b = 255, 255
# print(id(a), id(b))
#
# a, b = 20_000_000, 20_000_000
# print(id(a), id(b))
#
# a = 30_000_000
#
# b = 30_000_000
#
# print(id(a), id(b))

string1 = "I sleep all night, and work all day"
s = iter(string1)
print(s)