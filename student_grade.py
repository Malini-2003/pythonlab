def print_report(student_name, grade):
    print("********************** REPORT **********************")
    print(f"Student Name: {student_name}")

    if grade == 'A':
        print(f"Grade: {grade} ")
    elif grade == 'B':
        print(f"Grade: {grade}")
    elif grade == 'C':
        print(f"Grade: {grade} ")
    elif grade == 'D':
        print(f"Grade: {grade} ")
    elif grade == 'F':
        print(f"Grade: {grade} ")
    else:
        print("Invalid grade entered.")

    print("*******************************************************")

student_name = input("Enter the student's name: ")
grade = input("Enter the student's grade: ")

print_report(student_name, grade)
