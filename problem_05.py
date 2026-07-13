# Problem 5/100 — Leap Year Checker

# User se year input lo aur check karo ki year leap year hai ya nahi.

# Rules:

# * Year 400 se divisible → Leap year
# * Otherwise 100 se divisible → Not leap year
# * Otherwise 4 se divisible → Leap year
# * Otherwise → Not leap year

# Examples: 2000 → Leap year, 1900 → Not leap year, 2024 → Leap year, 2025 → Not leap year.

year = int(input("Enter the year"))
if year%400 == 0 or year%4 == 0 and year%100 !=0:
    print("This is a leap year:")
else:
    print("This year is not a leap year:")