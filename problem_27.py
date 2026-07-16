# Problem 27/100 — Student Result Management System

# Problem Statement:
# Create a Student Result Management System.

# User se pehle number of students input lo.

# Example:
# Enter number of students: 3

# Har student ke liye input lo:
# - Student Name
# - Marks in English
# - Marks in Math
# - Marks in Science

# Store the data in a dictionary.

# Example:
# {
#     "Rahul": [85, 90, 78],
#     "Aman": [65, 70, 60],
#     "Priya": [95, 92, 98]
# }

# Create the following menu:

# ===== MENU =====
# 1. Show All Students
# 2. Search Student
# 3. Update Marks
# 4. Show Toppers
# 5. Exit

# Option 1:
# Display all students with their marks.

# Example:
# Rahul : [85, 90, 78]
# Aman : [65, 70, 60]

# Option 2:
# Search a student by name.
# If found, display:
# Name
# English Marks
# Math Marks
# Science Marks
# Total Marks
# Percentage
# Grade

# Grade Rules:
# 90 and above -> A
# 80-89 -> B
# 70-79 -> C
# 60-69 -> D
# Below 60 -> F

# Option 3:
# Update marks of any one subject.

# Example:
# Enter Student Name: Rahul
# Which Subject?
# 1. English
# 2. Math
# 3. Science

# Enter New Marks: 95

# Update Successfully!

# Option 4:
# Display the student who has the highest total marks.

# Example:
# Topper: Priya
# Total Marks: 285

# Option 5:
# Exit the program.

# Rules:
# 1. Use Dictionary.
# 2. Store marks in a List.
# 3. Use Functions.
# 4. Use Menu.
# 5. Do not use max(), min(), sum(), sorted().

# Concepts Practiced:
# - Dictionary
# - List
# - Functions
# - Loops
# - Conditions
# - Nested Data Structures

# Bonus (Optional):
# Show class average marks in each subject.

students_record = {}
def show_students_record(students_record):
    print("\n ---------Students Marks---------")
    for student, subjects in students_record.items():
        print(f"\nStudent: {student}")
        for subject, marks in subjects.items():
            print(f"  {subject:<8}: {marks}")

def input_student_marks(students_record):
            name = input("Enter student name:")
            english = int(input("Enter English Marks:"))
            hindi = int(input("Enter Hindi Marks:"))
            math = int(input("Enter Math Marks:"))
            python = int(input("Enter Python Marks:"))
            dsa = int(input("Enter DSA Marks:"))
            students_record[name] = {
                "English": english,
                "Hindi": hindi,
                "Math": math,
                "Python": python,
                "DSA": dsa
            }
       
def create_students_record(students_record):
    no_of_students = int(input("Enter number of students:"))
    for i in range(no_of_students):
        input_student_marks(students_record)
    show_students_record(students_record)

def add_students_record(students_record):
    input_student_marks(students_record)
    show_students_record(students_record)

def search_student(students_record):
    student_name = input("Enter Student Name:")
    if student_name in students_record:
        print("Name: ",student_name)
        for subject, marks in students_record[student_name].items():
            print(subject, ":", marks)
        total = 0
        for marks in students_record[student_name].values():
            total+=marks
        print("Total Marks: ",total)
        percentage = (total/500)*100
        print("Percentage: ",percentage)
        if percentage>=90:
            print("Grade: A+")
        elif percentage>=80:
            print("Grade: A")
        elif percentage>=70:
            print("Grade: B")
        elif percentage>=60:
            print("Grade: C")
        elif percentage>=50:
            print("Grade: D")
        elif percentage<50:
            print("Grade: F")
    else:
        print("Student does not exists.")
        
def update_marks(students_record):
    student_name = input("Enter Student Name:")
    if student_name in students_record:
        print("\n=====Which Subject=====")
        subjects = ["English", "Hindi", "Math", "Python", "DSA"]
        for i in range(len(subjects)):
            print(i+1,".",subjects[i])
        which_subject = int(input("Choose a option:"))
        if 1 <= which_subject <= len(subjects):
            subject = subjects[which_subject-1]
            new_marks = int(input("Enter new marks: "))
            students_record[student_name][subject]=new_marks
            print("Update Successfully!")
            show_students_record(students_record)
        else:
            print("Invalid subject choice.")
    else:
        print("Student does not exist.")
        
def show_toppers(students_record):
    highest_total = -1
    topper = ""
    for key,value in students_record.items():
        total = 0
        for marks in value.values():
            total+=marks
        if total>highest_total:
            highest_total=total
            topper=key
    print("Topper: ",topper)
    print("Total: ",highest_total)

while True:
    print("\n======Menu======")
    print("1. Create Students Marks Record")
    print("2. Add Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Show Toppers")
    print("6. Show All Students")
    print("7. Exit")
    choice = int(input("Choose a option:"))
    
    if choice == 1:
        create_students_record(students_record)
    elif choice == 2:
        add_students_record(students_record)
    elif choice == 3:
        search_student(students_record)
    elif choice == 4:
        update_marks(students_record)
    elif choice == 5:
        show_toppers(students_record)
    elif choice == 6:
        show_students_record(students_record)
    elif choice == 7:
        print("GoodBye!")
        break
    else:
        print("Invalid Choice.")