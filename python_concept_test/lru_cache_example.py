from functools import lru_cache


@lru_cache
def my_fun2(a, b):
    print("Calculating a+b ...")
    return a+b

print(my_fun2(1, 5))
print(my_fun2(1, 5))
print(my_fun2(1, 5))




