# Problem 12/100 — Character Counter

# User se ek sentence input lo aur count karo:

# * vowels
# * consonants
# * digits
# * spaces

# Example: Hello 123 → Vowels: 2, Consonants: 3, Digits: 3, Spaces: 1.

# Rule: a, e, i, o, u ko vowels maanna hai, uppercase vowels bhi handle karne hain.

sentence = input("Enter your thoughts:")
vowels = 0
consonants = 0
digits = 0
spaces = 0
for i in sentence:
    if i == " ":
        spaces += 1
    if i in "0123456789":
        digits += 1
    if i in "aeiouAEIOU":
        vowels += 1
    if i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        consonants += 1
print("Vowels = ",vowels)
print("Consonants = ",consonants)
print("Digits = ",digits)
print("Spaces = ",spaces)