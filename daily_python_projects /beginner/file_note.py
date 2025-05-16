# This is store note of user into the file

FILENAME = "notes.txt"

# Step 1: Ask the user for a note
note = input("Write a note : ")
print(type(note))

# Step 2: Save the note to a file
with open(FILENAME,"a") as file:
    # print("Note saved! 📝")
    print(type(file))
    # file.write(note + "\n")
    # print("Note saved! 📝")
