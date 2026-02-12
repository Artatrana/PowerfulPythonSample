list1 = [1,2,3,4,5,6,7,8]

val1, val2, *rest = list1

print(val1, val2, rest)

first_val, *_, last_val  = list1

print(first_val, last_val )

data = [
    ("user1", 100001, "Admin"),
    ("user2", 100002, "Admin", "moderator", "user"),
    ("user3", 100003, "moderator", "user"),
]
for name, userid, *roles in data:
    print(f"Name: {name}, Userid: {userid}, Roles: {roles}")

for num, value in [(1,'football'),(2,'cricket'),(3,'baseball')]:
    print(num, value)

