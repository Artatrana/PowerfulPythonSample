# Solution: Generate Indexed List with Python
mylist = ['a', 'b', 'c']
# Create a empty list to store the tuples
index_list = []

# Using a for loop to iterate over the list with enumeration
for idx, item in enumerate(mylist):
    index_list.append((item, idx))

# Printing the original list and the indexed list
print("Indexed list:", index_list)