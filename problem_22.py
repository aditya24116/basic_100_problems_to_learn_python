# Problem 22/100 — Student Marks Manager

# Ye pehla mini real-world problem hai.

# Problem Statement

# User se pehle number of students lo.

# Example:
#     Enter number of students: 3
    
# Uske baad har student ka:

# * Name
# * Marks

# Input lo.

# Example:
#     Enter student name: Rahul
#     Enter marks: 90

#     Enter student name: Aman
#     Enter marks: 75

#     Enter student name: Priya
#     Enter marks: 88
    
# Store as:
#     {
#     "Rahul": 90,
#     "Aman": 75,
#     "Priya": 88
# }
    
# Finally print:

# Student Records
# Rahul : 90
# Aman : 75
# Priya : 88

# Rules

# * ✅ Dictionary use karni hai.
# * ✅ Loop use karna hai.
# * ❌ List use nahi karni.
# * ❌ Hardcoded values nahi.

# 🎯 Challenge

# Bonus feature (optional):

# Program ke end mein user se ek student name pucho:
# Enter student name to search:
# Agar dictionary mein hai:
# Marks: 90
# Nahi hai:
# Student not found.


number_of_students = int(input("Enter number of students:"))
students_details = {}
for i in range(number_of_students):
    name = input("Enter student name:")
    marks = int(input("Enter student marks:"))
    students_details[name]=marks
for name in students_details:
    print(name, ":", students_details[name])
search = input("Enter student name:")
if search in students_details:
    print("Marks:",students_details[search])
else:
    print("Student not found:")