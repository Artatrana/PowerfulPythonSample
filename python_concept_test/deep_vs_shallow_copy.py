a = [1, 2, [10, 20]]
b = a.copy()
print(id(a), id(a[0]),id(a[1]) ,id(a[2]))
b[2].append(30)
print(a)  # [1, 2, [10, 20, 30]]
print(b)  # [1, 2, [10, 20, 30]]

print(id(b),id(b[0]),id(b[1]) ,id(b[2]))

from copy import deepcopy

print('=' * 80)
print("Experiment with deep copy")

a = [1, 2, [10, 20]]
b = deepcopy(a)
print(id(a), id(a[0]),id(a[1]) ,id(a[2]))
b[2].append(30)
print(a)  # [1, 2, [10, 20, 30]]
print(b)  # [1, 2, [10, 20, 30]]

print(id(b),id(b[0]),id(b[1]) ,id(b[2]))







