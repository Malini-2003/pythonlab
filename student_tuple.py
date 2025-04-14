# List to store student tuples
students = []

# 1. Create Students
def create_students():
    global students
    students = [
        ("Malini", 101, (85, 90, 88), "A"),
        ("Sherin", 102, (75, 80, 78), "B"),
        ("Nausheen", 103, (65, 70, 68), "C")
    ]
    print("Initial student data created.\n")

# 2. Display All Students
def display_all_students():
    if not students:
        print("No student records found.\n")
        return
    print("Student Records:")
    for student in students:
        name, roll, marks, grade = student
        print(f"Name: {name}, Roll No: {roll}, Marks: {marks}, Grade: {grade}")
    print()

# 3. Add a New Student
def add_student(name, roll, marks, grade):
    student = (name, roll, marks, grade)
    students.append(student)
    print(f"Student '{name}' added successfully.\n")

# 4. Search for a Student
def search_student(roll):
    for student in students:
        if student[1] == roll:
            name, roll, marks, grade = student
            print(f"Student Found - Name: {name}, Roll No: {roll}, Marks: {marks}, Grade: {grade}\n")
            return
    print("Student not found.\n")

# 5. Calculate Total Marks for Each Student
def calculate_total_marks():
    print("Total Marks of Students:")
    for student in students:
        name, roll, marks, grade = student
        total = sum(marks)
        print(f"Name: {name}, Roll No: {roll}, Total Marks: {total}")
    print()

# 6. Update Grades
def update_grade(roll, new_grade):
    global students
    for i in range(len(students)):
        if students[i][1] == roll:
            name, roll_no, marks, _ = students[i]
            students[i] = (name, roll_no, marks, new_grade)
            print("Grade updated successfully.\n")
            return
    print("Student not found.\n")

# 7. Remove a Student
def remove_student(roll):
    global students
    for i in range(len(students)):
        if students[i][1] == roll:
            removed = students.pop(i)
            print(f"Student '{removed[0]}' removed successfully.\n")
            return
    print("Student not found.\n")
# Create initial data
create_students()

# Display all students
display_all_students()

# Add a new student
add_student("Chaya", 104, (90, 92, 95), "A")

# Search for a student
search_student(102)

# Calculate total marks
calculate_total_marks()

# Update a student's grade
update_grade(103, "B+")

# Remove a student
remove_student(101)

# Final display
display_all_students()
