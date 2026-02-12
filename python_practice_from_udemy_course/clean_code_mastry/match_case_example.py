role = input("Enter your role: ")

if role == "admin":
    print("Welcome Admin! You have full access")
elif role == "moderator":
    print("Welcome Moderator! You can manage user content")
elif role == "user":
    print("Welcome user! Enjoy browsing your platform. ")
else:
    print("Unrecognized role. ")

match role:
    case "admin":
        print("Welcome Admin! You have full access")
    case "moderator":
        print("Welcome Moderator! You can manage user content")
    case "user":
        print("Welcome user! Enjoy browsing your platform. ")
    case _:
        print("Unrecognized role. ")