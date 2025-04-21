student_marks = {
    "Malini": 85,
    "Sherin": 78,
    "Nausheen": 92,
    "Diya": 88,
    "Chaya": 74
}

name = input("Enter the student's name: ")

if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"No record found for student named '{name}'.")
