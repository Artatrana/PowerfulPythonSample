class Animal:
    def __init__(self, type):
        self.type = type

    def print_type(self):
        print(f"Type of the animal {self.type}")

# ID of the class
# print(id(Animal))
#
# # ID of the function object inside the class
# print(id(Animal.print_type))

# ID of the bound method via an instance
a = Animal("Lion")
# print(id(a))   # Different from Animal.print_type
# print(id(a.print_type))   # Different from Animal.print_type

list1 = ["test1", "est", "eppppske", "testuesetere"]
var_map = map(len, list1)
print( list(var_map))

