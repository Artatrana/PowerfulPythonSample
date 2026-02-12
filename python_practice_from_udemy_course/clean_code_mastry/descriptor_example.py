# Any class that implements __get__ or __set__ or __delete___ is called Descriptor
# What is the primary purpose of a Descriptor ? A descriptor allow a class to control what happens when an attribute is
# accessed, set or deleted. In simple term, it centralizes attribute behavior instead of scattering logic across many classes.
# What kind of problem it solves - It solves the problem of repeated, inconsistent attribute logic ( like validataion, computed values,
# or lazy loading). You define the rule once and reuse it everywhere, keeping code cleaner and more predictable.

# class Descriptor:
#     def __init__(self):
#         self._value = None  # Store the value here
#
#     def __get__(self, instance, owner):
#         print("Getting value...")
#         return self._value
#     def __set__(self, instance, value):
#         print(f"Setting value to {value}")
#         self._value = value
#
# class MyClass:
#     attribute = Descriptor()
#
# obj = MyClass()
# obj.attribute = 100 # ? why attribute work - attribute is a object - how will it know which method being called - like get, set or delete
# print(obj.attribute)
#
# obj = MyClass()
# obj.attribute = 0
# print(obj.attribute)


# class Height():
#     def __init__(self, value):
#         self._height = value
#     def height(self):
#         return self._height
#
# class Animal:
#     #ani_height = Height(10)
#
#     def __init__(self, leg, height):
#         self._leg = leg
#         self.ani_height = Height(height)
#
#     def get_height_leg(self):
#         print( f"Animal has {self._leg} legs and Height {self.ani_height.height()}")
#
# animal1 = Animal(4, 10)
# print(animal1.get_height_leg())
#
# animal1 = Animal(2, 20)
# print(animal1.get_height_leg())


class AgeValidator:
    def __get__(self, instance):
        return instance.__dict__.get("_age")

    def __set__(self, instance, value):
        if value < 0 or value > 120:
            raise ValueError("Age must be between 0 and 120")
        instance.__dict__["_age"] = value

class Teacher:
    age = AgeValidator()

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Athletes:
    age = AgeValidator()

    def __init__(self, name, age):
        self.name = name
        self.age = age

t = Teacher("Alice", 40)     # OK
a = Athletes("Bob", 25)      # OK

#t.age = 130