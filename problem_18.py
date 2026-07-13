# Problem 18/100 — Second Largest Number

# Input:
#     10 45 23 89 67 89 12
    
# Output:
#     Second Largest Number: 67
    
# Rules

# * ❌ sort() use nahi karna.
# * ❌ max() use nahi karna.
# * ✅ Sirf loops aur if conditions.
# * Duplicate largest values ignore karni hain.

# Example:

# Input:
#     5 8 8 3 1
    
# Output:
#     5

numbers = list(map(int, input("Enter numbers: ").split()))

if len(numbers) < 2:
    print("Please enter at least two numbers.")
else:
    greatest = numbers[0]
    second_greatest = None

    for number in numbers:
        if number > greatest:
            second_greatest = greatest
            greatest = number
        elif number != greatest and (
            second_greatest is None or number > second_greatest):
            second_greatest = number

    if second_greatest is None:
        print("There is no second greatest number.")
    else:
        print("Greatest Number:", greatest)
        print("Second Greatest Number:", second_greatest)
