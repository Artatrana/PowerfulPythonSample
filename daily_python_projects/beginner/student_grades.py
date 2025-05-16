# Initial dictionary of students and their grades
def student_garde():
    grades = {
        "Alice": 78,
        "Bob": 42,
        "Charlie": 65,
        "Diana": 49,
        "Eve": 90
    }

    # Create a new dictionary to categorize students
    categories = {}
    for student, grade in grades.items():
        if grade >= 50:
            categories[student] = "Pass"
        else:
            categories[student] = "Fail"

    # Print the categorized dictionary
    print("Student Categories:")
    for student, status in categories.items():
        print(f"{student}: {status}")


if __name__ =="__main__":
    student_garde()
