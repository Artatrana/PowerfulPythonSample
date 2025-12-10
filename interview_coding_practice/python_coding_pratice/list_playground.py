# This is a general trial and error code to implement different attribute of lists

lst = [[-1,-1,2],[-1,0,1],[-2,0,1],[31,0,1]]
lst.sort()
# print(lst )
# print(sorted(lst))

d = {"b": 2, "a": 1, "c": 3}

# # # Works with sorted() — by default, sorts keys
# # print(sorted(d))        # ['a', 'b', 'c']
# #
# # # Can also sort items by value
# # print(sorted(d.items(), key=lambda x: x[1]))
# # # [('a', 1), ('b', 2), ('c', 3)]
#
# #print(sorted(d, key=lambda x: x[0]))
# # [('a', 1), ('b', 2), ('c', 3)]
# print(d)

words = ("banana", "apple", "cherry")
print(type(words))
print(words)

gen = (w for w in words)   # generator
print(gen)
print(type(gen))
print(next(gen))
print(next(gen))

# #words_list = [w for w in words]
gen_list = list(gen)
print(gen_list)


lit_words = iter(list(words))
print(type(lit_words))
print(next(lit_words))
print(next(lit_words))

lit_words_lst = list(lit_words)
print(lit_words_lst)


