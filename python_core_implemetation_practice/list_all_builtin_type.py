# This program will list all built-in method

# import builtins
#
# builtins_types = [obj for obj in builtins.__dict__.values() if isinstance(obj, type)]
#
# print("Total built-in types:", len(builtins_types))
# print(builtins_types[:20])  # show first 20

# sorted() → Sorted iterable
print("sorted():", sorted([3, 1, 2]))  # [1, 2, 3]
print("reversed() : " , list(reversed([3, 1, 2])))
print("reversed() : " , list(reversed(sorted([3, 1, 2]))))