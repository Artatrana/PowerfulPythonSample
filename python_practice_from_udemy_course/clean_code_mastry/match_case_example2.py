event = {"type":"error", "code":404, "message":"Not found"}

match event:
    case {"type":"error", "code": code, "message":message}:
        print(f"Error {code}: {message}")
    case {"type":"warning", "message": message}:
        print(f"Warning {message}")
    case {"type": "info", "message": message}:
        print(f"Info {message}")
    case _:
        print("Unknown event type")

# Another example
users = [("Alice", "admin"), ("Bob", "moderator"),("Cahrlie", "user")]
for user in users:
    match user:
        case (name, "admin"):
            print(f"{name} is an admin with full access !")
        case (name, "moderator"):
            print(f"{name} is a moderator with content management privileges !")
        case (name, "user"):
            print(f"{name} is a regular user !")
        case _:
            print("Unknown role")

role = input("Enter your role")
match role:
    case "admin" | "moderator":
        print("Welcome ! you have management privilege. ")
    case "user":
        print("Welcome, user Enjoy browsing. ")
    case _:
        print("Unrecognized role")

# But when you use constant to match patter: You need to careful
# Its better to use Enumeration instead of simple constant

from enum import Enum
class Role(Enum):
    ADMIN = "admin"
    USER = "user"

def handel_role(role):
    match role:
        case Role.ADMIN:
            print("Welcome ! you have management privilege. ")
        case Role.USER:
            print("Welcome, user Enjoy browsing. ")
        case _:
            print("Unrecognized role")

handel_role(Role.ADMIN)


