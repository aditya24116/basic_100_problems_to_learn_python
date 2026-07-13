# Problem 19/100 — Most Frequent Element

# Problem Statement

# User enters numbers:
#     Enter numbers: 1 2 2 3 4 2 5 3 3 3
    
# Output:
#     Most Frequent Element: 3
#     Frequency: 4

# Rules

# * ✅ Use a dictionary.
# * ❌ Do not use count().
# * ❌ Do not use max().
# * ❌ Do not use sort().
# * ✅ Use loops.

# ⸻

# Example 2

# Input:
#     5 5 3 2 5 3 2 3 3

# Output:
#     Most Frequent Element: 3
#     Frequency: 4

numbers = list(map(int,input("Enter the numbers:").split()))
numbers_dict = {}
highest_frequency = 0
most_frequent = None
for i in numbers:
    if i in numbers_dict:
        numbers_dict[i]+=1
    else:
        numbers_dict[i]=1
for key in numbers_dict:
    if numbers_dict[key]>highest_frequency:
        highest_frequency=numbers_dict[key]
        most_frequent= key
print("Most Frequent Element:",most_frequent)
print("Highest Frequency:",highest_frequency)