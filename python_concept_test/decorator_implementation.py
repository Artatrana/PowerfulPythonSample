
# Defining a decorator
def memoizer(fn):
    cache = {}
    def inner(*args, **kwargs):
        key = frozenset(args)| frozenset(kwargs.items())
        if key in cache:
            return cache[key]
        else:
            result = fn(*args, **kwargs)
            cache[key] = result
            return result
    return inner

@memoizer
def adder(*args):
    print("Calculating the result")
    return sum(args)

print(adder(*[2,4,5]))
print(adder(*[4,5,2]))
print(adder(*[5,4,2]))



