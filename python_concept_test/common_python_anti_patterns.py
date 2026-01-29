# 2.1. Using mutable default arguments

# ❌ Anti-pattern
def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

append_to_list(1)  # [1]
append_to_list(2)  # [1, 2]  ← unintended shared state
print(append_to_list(2) )

# Good alternative:
def append_to_list_updated(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list

append_to_list_updated(1)  # [1]
append_to_list_updated(2)  # [1, 2]  ← unintended shared state
print(append_to_list_updated(2) )

# 2.2. Catching generic exceptions
# Why bad: Hides real errors, makes debugging hard.
# ❌ Anti-pattern
def risky_code(): pass

try:
    risky_code()
except Exception:
    print("Something went wrong!")

try:
    risky_code()
except ValueError:
    print("Something went wrong!")

# 2.3. Overusing *args / **kwargs
# ❌ Anti-pattern
def my_function(*args, **kwargs):
    risky_code(args, kwargs)

# Why bad: Obscures API, hard for others to understand or maintain.
# Good alternative: Explicit parameters wherever possible.

# 2.4 Deeply nested
# ❌ Anti-pattern
# if cond1:
#     if cond2:
#         if cond3:
#             do_something()

# Why bad: Hard to read and maintain.
# Good alternative: Use guard clauses:
#
# if not cond1:
#     return
# if not cond2:
#     return
# if not cond3:
#     return
# do_something()

# 2.5 Using bare return None for error signaling
# ❌ Anti-pattern
def get_user(id):
    if not id_exist(id):
        return None
# Why bad: Leads to silent failures when None is propagated.
# Good alternative: Raise an exception or use Optional type hints.

# 2.6 Reinventing the wheel
# ❌ Anti-pattern
my_sum = 0
for x in my_list:
    my_sum += x

# Why bad: Python has built-in, optimized solutions:
my_sum = sum(my_list)

# 2.7. Using global variables excessively
# ❌ Anti-pattern
counter = 0
def increment():
    global counter
    counter += 1
# Why bad: Hard to track state, thread-unsafe.
# Good alternative: Encapsulate in a class or pass as parameter.

# 2.8. Shadowing built-in names
# ❌ Anti-pattern
list = [1, 2, 3]  # overrides built-in 'list'

# Why bad: Can cause subtle bugs later.
# Good alternative: Use descriptive variable names.

# 2.9. Excessive one-liners
# ❌ Anti-pattern
result = [do(x) for x in items if check(x) and update(x) or True]

# Why bad: Hard to read, hard to debug.
# Good alternative: Break into multiple lines with clear logic.