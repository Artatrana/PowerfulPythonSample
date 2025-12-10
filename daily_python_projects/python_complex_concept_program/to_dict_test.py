# Testing how to_dict function work

employee_name =["Test1", "Test2", "Test3"]
employee_id = [1,2,3]

employee_zip = zip(employee_id,employee_name)
# print(employee_zip)
# print(dict(employee_zip))

list1 = [1,2,3,5]
print(id(list1))
list1.append(4)
print(list1, id(list1))
list1.extend([4,5,6])
print(list1, id(list1))

lst = [1, 2, 3]
print("Before:", id(lst))
lst = list(lst)
print("After: ", id(lst))

lst = [1, 2, 3]
print("Before:", id(lst))

lst = lst[:]

print("After: ", id(lst))