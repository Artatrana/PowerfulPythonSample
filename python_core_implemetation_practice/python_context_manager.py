class DatabaseConnection:
    """ The calss to demonstrate Context manager of python"""

    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False

    def __enter__(self):
        """"Establish a connection """
        self.connected = True
        print(f"Connected to the database {self.db_name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close the connection"""
        self.connected=False
        print(f"Disconnected from the database {self.db_name}")
        if exc_type:
            print(f"An exception occurred: {exc_val}")
        return True # Supress exceptions if they occur



class MyContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"Exception caught: {exc_type}, {exc_value}")
            return True  # suppress exception
        print("Exiting normally")

with MyContext():
    x = 1 / 0   # raises exception, caught by __exit__()

"""" Example of exc_type, exc_value, traceback"""
import sys

try:
    1/0
except:
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(exc_type)
    print(exc_value)
    print(exc_tb)

print(dir("hello"))