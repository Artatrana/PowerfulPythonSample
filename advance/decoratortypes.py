# Class Decoratorsz: These are decorators that are applied to classes instead of functions. 
# They can modify or enhance the class definition.Used to modify class behavior or add additional methods or attributes.

def add_class_method(cls):
    cls.new_method = lambda self: "New Method Added!"
    return cls

@add_class_method
class MyClass:
    pass

# obj = MyClass()
# print(obj.new_method())  # Output: New Method Added!

# 2. Method Decorators
# These are decorators specifically for instance methods within a class.
# Often used to implement functionality like access control, method logging, or performance monitoring for class methods.

def method_decorator(method):
    def wrapper(self, *args, **kwargs):
        print(f"Method {method.__name__} is called")
        return method(self, *args, **kwargs)
    return wrapper

class MyClass:
    @method_decorator
    def my_method(self):
        print("Inside My Method")

# obj = MyClass()
# obj.my_method()  # Output: Method my_method is called \n Inside My Method

# 3. Static and Class Method Decorators 
# These decorators are used to define static methods and class methods in a class.
# Usage: @staticmethod and @classmethod allow defining methods that are not bound to an instance of the class or are bound to the class itself.
        
class MyClass:
    @staticmethod
    def static_method():
        return "Static Method Called"
    
    @classmethod
    def class_method():
        return "Class Method Called"
        
    
