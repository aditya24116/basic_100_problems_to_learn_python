# Problem 26/100 — Student Attendance Manager

# Problem Statement:
# Create a Student Attendance Management System.

# User se pehle number of students input lo.

# Example:
# Enter number of students: 3

# Har student ke liye input lo:
# - Student Name
# - Attendance Percentage

# Dictionary Format:
# {
#     "Rahul": 92,
#     "Aman": 68,
#     "Priya": 81
# }

# Menu:
#
# ===== MENU =====
# 1. Show All Students
# 2. Search Student
# 3. Update Attendance
# 4. Show Eligible Students
# 5. Exit

# Option 1:
# Print all students with attendance.

# Example:
# Rahul : 92%
# Aman : 68%
# Priya : 81%

# Option 2:
# User enters a student name.
# If found:
# Rahul : 92%
# Otherwise:
# Student not found.

# Option 3:
# User enters student name.
# User enters new attendance percentage.
# Update the dictionary.

# Example:
# Enter student name: Aman
# Enter new attendance: 75
# Updated Successfully!

# Option 4:
# Print only students whose attendance is 75% or more.

# Example:
# Eligible Students

# Rahul : 92%
# Priya : 81%

# Option 5:
# Exit the program.

# Rules:
# 1. Use Dictionary.
# 2. Use Functions.
# 3. Use While Loop.
# 4. Use Menu.
# 5. Do not use classes.

# Concepts Practiced:
# - Dictionary
# - Functions
# - Loops
# - Conditions
# - Menu Driven Program

# Bonus (Optional):
# After updating attendance, immediately display the updated attendance list.
def create_students (students_attendance,num_of_students):
    for i in range(num_of_students):
        name = input("Enter Student Name:")
        attendance = int(input("Enter Student Attendance:"))
        students_attendance[name]=attendance
    show_attendance(students_attendance)
def add_students (students_attendance):
    name = input("Enter Student Name:")
    attendance = int(input("Enter Student Attendance:"))
    students_attendance[name]=attendance
    show_attendance(students_attendance)
def show_attendance (students_attendance):
    print("\n------Students Attendance-------")
    for key,value in students_attendance.items():
        print(f"{key}:{value}%")
def search_student (students_attendance):
    name = input("Enter the Student Name:")
    if name in students_attendance:
        print(name, ":", students_attendance[name])
    else:
        print("Student dose not exists.")
def update_attendance (students_attendance):
    name = input("Enter Student Name:")
    if name in students_attendance:
        new_attendance = int(input("Enter New Attendance:"))
        students_attendance[name]=new_attendance
        print("Updated successfully.")
    else:
        print("Student Not found.")
    show_attendance(students_attendance)
def show_eligible_students (students_attendance):
    print("\n----- Eligible Students -----")
    for name,attendance in students_attendance.items():
        if attendance>=75:
            print(f"{name} : {attendance}%")
num_of_students =int(input("Enter the number of students:"))
students_attendance = {}
create_students(students_attendance,num_of_students)
while True:
    print("\n===== MENU =====")
    print("1. Add Students:")
    print("2. Search Student:")
    print("3. Update Attendance:")
    print("4. Show eligible Students:")
    print("5. Exit")
    choice = int(input("Enter Your choice:"))
    
    if choice == 1:
        add_students(students_attendance)
    elif choice==2:
        search_student(students_attendance)
    elif choice==3:
        update_attendance(students_attendance)
    elif choice==4:
        show_eligible_students(students_attendance)
    elif choice==5:
        print("Goodbye!")
        break
    else:
        print("Plese enter a valid choice:")