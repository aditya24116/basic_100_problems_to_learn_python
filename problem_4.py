# Problem 4/100 — Number Type Checker

# User se ek number lo aur check karo ki woh:

# * Positive hai
# * Negative hai
# * Zero hai
# Example:
#     Enter a number: -8
#     The number is negative.

Number =float(input("Enter the number"))
if Number > 0:
    print("This number is Positive.")
elif Number == 0:
    print("This number is Zero.")
elif Number < 0:
    print("This number is Negative.")