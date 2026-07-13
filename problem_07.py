# Problem 7/100 — Student Percentage & Grade Calculator

# User se 5 subjects ke marks lo. Har subject 100 marks ka hai. Calculate karo: total marks, percentage, aur grade.

# Grade rules: 90+ → A+, 80–89 → A, 70–79 → B, 60–69 → C, 50–59 → D, <50 → F.

# Example output:
#     Total Marks: 412/500
#     Percentage: 82.4%
#     Grade: A

English = int(input("Enter your number in English:"))
Hindi = int(input("Enter your number in Hindi:"))
Math = int(input("Enter your number in Math:"))
Python = int(input("Enter your number in Python:"))
dsa = int(input("Enter your number in dsa:"))
total_marks = English+Hindi+Math+Python+dsa
percentage = total_marks/5
print(f"Total Marks: {total_marks}/500")
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
else:
    print("Grade: F")