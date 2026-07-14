# Problem 25/100 — Student Grade Analyzer

# Problem Statement:
# Create a Student Grade Analyzer using a dictionary.

# User se pehle number of students input lo.

# Example:
# Enter number of students: 3

# Phir har student ke liye:
# - Student Name
# - Marks

# Dictionary format:
# {
#     "Rahul": 85,
#     "Aman": 72,
#     "Priya": 94
# }

# Ab program ko ye sab print karna hai:

# ===== REPORT =====

# Highest Marks:
# Priya : 94

# Lowest Marks:
# Aman : 72

# Average Marks:
# 83.67

# Grade Report:
# Rahul : B
# Aman : C
# Priya : A

# Grade Rules:
# Marks >= 90  -> A
# Marks >= 80  -> B
# Marks >= 70  -> C
# Marks >= 60  -> D
# Marks < 60   -> F

# Rules:
# 1. Dictionary use karni hai.
# 2. max(), min(), sum(), sorted() use nahi karna.
# 3. Sirf loops aur if-else use karna.
# 4. Highest aur Lowest manually find karne hain.
# 5. Average manually calculate karna hai.

# Concepts Practiced:
# - Dictionary
# - Loops
# - Conditions
# - Variables
# - Algorithm Design

# Bonus (Optional):
# Program ke end me user se ek student ka naam pucho.
# Agar student exist karta hai to uske marks aur grade print karo.
# Nahi to print karo:
# Student not found.

def report(students_details):
    print("\n----- Report Card -----")
    highest_marks = -1
    highest_student = ""
    lowest_marks = 101
    lowest_student = ""
    total_marks = 0
    for student, marks in students_details.items():
        total_marks+=marks
        if marks > highest_marks:
            highest_marks = marks
            highest_student = student
        if marks < lowest_marks:
            lowest_marks = marks
            lowest_student = student
        if marks >= 90:
            grade = "A"
        elif marks >= 80:
            grade = "B"
        elif marks >= 70:
            grade = "C"
        elif marks >= 60:
            grade = "D"
        else:
            grade = "F"
        print(student, ":", grade)
    average_marks = total_marks/len(students_details)
    print("Highest scored student name:",highest_student)
    print("Highest Marks:",highest_marks)
    print("Lowest scored student name:",lowest_student)
    print("Lowest Marks:",lowest_marks)
    print("Average Marks:",average_marks)    
def show_students(students_details):
    print("\n----- Current Students -----")

    for key, value in students_details.items():
        print(f"{key} : {value}")

def create_students_dict(Number_of_students):
    for i in range(Number_of_students):
        student_name = input("Enter Student Name:")
        student_marks = int(input("Enter marks of student:"))
        students_details[student_name] = student_marks
    show_students(students_details)
Number_of_students = int(input("Enter number of the students:"))
students_details = {}
highest_marks = -1
highest_student = ""
lowest_marks = 101
lowest_student = ""
create_students_dict(Number_of_students)
report(students_details)
