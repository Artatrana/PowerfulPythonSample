# Dictionary for examples
my_dict = {"a": 1, "b": 2, "c": 3}


# 3. fromkeys() → Creates dict from keys with a default value
keys = ["x", "y", "z"]
#print("fromkeys():", dict.fromkeys(keys, 0))  # {'x': 0, 'y': 0, 'z': 0}

test_dict2 = dict.fromkeys([1,2,3,4],)
#print ( test_dict2)

l1 , l2 = [1,2,3,4], ['one','two','three','four']
test_dict2 = dict(zip(l1,l2))
# print(type(test_dict2))
# #print(test_dict2.items())
# print(type(test_dict2.items()))
# print(type(test_dict2.keys()))
# print(type(test_dict2.values()))
for item in test_dict2.items():
    pass
    #print(item, type(item))

# print(type(test_dict2))
# print(type(test_dict2.items()))
# print(type(test_dict2.keys()))
# print(type(test_dict2.values()))

#

print(locals())

