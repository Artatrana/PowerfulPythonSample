# match-case example in python

def check_value(value):
    match value:
        case 1:
            print("The value is 1")
        case "hello":
            print("The value is 'hello'")
        case [1, 2, 3]:
            print("The value is a list: [1, 2, 3]")
        case int() as number if number > 10:
            print(f"The value is a number greater than 10: {number}")
        case str() as text:
            print(f"The value is a string: {text}")
        case _:
            print("The value does not match any case")


# Test the function
check_value(1)            # Matches case 1
check_value("hello")      # Matches case "hello"
check_value([1, 2, 3])    # Matches case [1, 2, 3]
check_value(15)           # Matches case int() > 10
check_value("Python")     # Matches case str()
check_value(3.14)         # Matches the default case
