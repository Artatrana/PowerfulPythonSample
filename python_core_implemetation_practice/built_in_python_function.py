# # return True or False
# for i in (bool(i) for i in [0, "",[], 1]) :
#     print(i)
# Python falsy construct
# print(bool(0))
# print(bool(0.0))
# print(bool(0j))
#
# print(bool([]))
# print(bool(()))
# print(bool(()))
# print(bool({} ))    # empty dict
# print(bool(set()))  # empty set
# print(bool(frozenset())) # empty frozenset
# print(bool(range(0)))   # empty range

# Frozenset (immutable)
# fs = frozenset([1, 2, 3])
# print(fs)      # frozenset({1, 2, 3})

# fs.add(4)  # ❌ ERROR: frozenset has no attribute 'add'

# === Python Built-in Functions Examples ===

# abs() → Absolute value
# print("abs():", abs(-5))  # 5

# all() → True if all elements are true
# print("all():", all([True, 1, "nonempty"]))  # True

# any() → True if any element is true
# print("any():", any([0, "", False, 42]))  # True

# ascii() → Returns a readable version of an object (escapes non-ASCII)
# print("ascii():", ascii("Ramesh 🚀"))  # 'Ramesh \U0001f680'

# bin() → Convert to binary string
# print("bin():", bin(8))  # '0b1000'

# bool() → Convert to boolean
# print("bool():", bool(""))  # False

# bytearray() → Create a mutable byte array
# print("bytearray():", bytearray([65, 66, 67]))  # bytearray(b'ABC')
# #b2 = bytearray("hello", "utf-8")
# print(bytearray("1234", "utf-8"))   # bytearray(b'hello')
#
# # bytes() → Immutable byte sequence
# print("bytes():", bytes([65, 66, 67]))  # b'ABC'
# # b4 = bytes(5)
# print( bytes(5))   # b'\x00\x00\x00\x00\x00'
#
# # callable() → Check if object is callable
# def test(): pass
# time_of = "test"
# print("callable():", callable(len))  # True
# print("callable():", callable(time_of))
# print("callable():", callable(test))

# # chr() → Unicode char from integer
# print("chr():", chr(65))  # 'A'

# # classmethod() → Define class method
# class Demo:
#     @classmethod
#     def show(cls):
#         return "class method"
# print("classmethod():", Demo.show())
#
# # compile() → Compile code into object
# code_obj = compile("5 + 10", "<string>", "eval")
# print("compile():", eval(code_obj))  # 15

# complex() → Create complex number
# print("complex():", complex(2, 3))  # (2+3j)
# z = complex(2, 3)
# print(z.real)  # 2.0
# print(z.imag)  # 3.0
# print(complex(5))

# # delattr() → Delete attribute
# class Car: pass
# c = Car()
# c.name = "Tesla"
# delattr(c, "name")
# print("delattr():", hasattr(c, "name"))  # False
#
# # dict() → Create dict
# print("dict():", dict(a=1, b=2))  # {'a': 1, 'b': 2}

# dir() → List attributes/methods
# print("dir() contains 'upper':", 'upper' in dir(str))  # True
# print(dir(str))

# # divmod() → Returns (quotient, remainder)
# print("divmod():", divmod(9, 4))  # (2, 1)
#
# # enumerate() → Index + item
# for i, v in enumerate(["a", "b"]):
#     print("enumerate:", i, v)

# # eval() → Evaluate expression
# print("eval():", eval("3 * 7"))  # 21
#
# # exec() → Execute code
# exec("x = 42")
# print("exec():", x)  # 42
#
# # filter() → Filter iterable
# nums = [1, 2, 3, 4]
# print("filter():", list(filter(lambda n: n % 2 == 0, nums)))  # [2, 4]
#
# # float() → Convert to float
# print("float():", float("3.14"))  # 3.14

# format() → Format string
# print("format():", format(255, "x"))  # 'ff'
# print(help(format))

# # frozenset() → Immutable set
# print("frozenset():", frozenset([1, 2, 3]))


# getattr() → Get attribute
# class User: name = "Ramesh"
# print("getattr():", getattr(User, "name"))  # Ramesh
#
# # globals() → Dictionary of global vars
# print("globals() contains '__name__':", "__name__" in globals())
# #print(globals())
#
# # hasattr() → Check attribute
# print("hasattr():", hasattr(User, "name"))  # True

# # hash() → Hash value
# print("hash():", hash("abc"))
#
# # help() → Interactive help system (skipping here to avoid long output)
#
# # hex() → Convert to hexadecimal
# print("hex():", hex(255))  # '0xff'
#
# # id() → Memory address (unique identifier)
# print("id():", id(42))

# input() → User input (commented out to avoid blocking)
# name = input("Enter name: ")

# # int() → Convert to integer
# print("int():", int("10"))  # 10
#
# # isinstance() → Type check
# print("isinstance():", isinstance(5, int))  # True
#
# # issubclass() → Subclass check
# print("issubclass(bool, int)):", issubclass(bool, int))  # True
#
# # iter() and next() → Iterators
# it = iter([1, 2, 3])
# print("next():", next(it))  # 1
#
# # len() → Length
# print("len():", len([1, 2, 3]))  # 3
#
# # list() → Create list
# print("list():", list("abc"))  # ['a', 'b', 'c']
#
# # locals() → Dictionary of local vars
# def demo():
#     x = 10
#     print("locals():", locals())
# demo()
#
#
# # map() → Apply function to iterable
# print("map():", list(map(str.upper, ["a", "b"])))  # ['A', 'B']
#
# # max() / min()
# print("max():", max(1, 5, 3))  # 5
# print("min():", min(1, 5, 3))  # 1

# # memoryview() → Memory view of object
# mv = memoryview(b"hello")
# print("memoryview():", mv[0])  # 104

# next() → Already shown above with iter

# # object() → Base object
# print("object():", object())
#
# # oct() → Octal string
# print("oct():", oct(8))  # '0o10'
#
# # open() → File handling (example skipped)
#
# # ord() → Unicode code point
# print("ord():", ord("A"))  # 65
#
# # pow() → Power
# print("pow():", pow(2, 3))  # 8
#
# # print() → Output
# print("print(): Hello World")

# property() → Manage attribute access
class Test:
    def __init__(self): self._x = 0
    def getx(self): return self._x
    def setx(self, v): self._x = v
    x = property(getx, setx)
t = Test()
t.x = 10
print("property():", t.x)

# # range() → Sequence
# print("range():", list(range(3)))  # [0, 1, 2]

# repr() → String representation
print("repr():", repr("hello\n"))  # "'hello\\n'"

# # reversed() → Reverse iterator
# print("reversed():", list(reversed([1, 2, 3])))

# # round() → Round number
# print("round():", round(3.14159, 2))  # 3.14

# # set() → Create set
# print("set():", set([1, 2, 2, 3]))  # {1, 2, 3}

# setattr() → Set attribute
setattr(t, "x", 20)
print("setattr():", t.x)  # 20

# slice() → Create slice object
s = slice(1, 3)
print("slice():", "hello"[s])  # 'el'

# # sorted() → Sorted iterable
# print("sorted():", sorted([3, 1, 2]))  # [1, 2, 3]

# # staticmethod()
# class Math:
#     @staticmethod
#     def add(a, b): return a + b
# print("staticmethod():", Math.add(2, 3))

# # str() → Convert to string
# print("str():", str(123))  # '123'
#
# # sum() → Sum iterable
# print("sum():", sum([1, 2, 3]))  # 6

# print("sum():", sum([3.2, 5]))

# super()
# class A:
#     def say(self): return "A"
# class B(A):
#     def say(self): return super().say() + " + B"
# print("super():", B().say())

# # tuple() → Create tuple
# print("tuple():", tuple([1, 2, 3]))

# # type() → Type of object
# print("type():", type(42))  # <class 'int'>

# vars() → __dict__ of object
print("vars():", vars(t))  # {'_x': 20}

# # zip() → Combine iterables
# print("zip():", list(zip([1, 2], ["a", "b"])))  # [(1, 'a'), (2, 'b')]

