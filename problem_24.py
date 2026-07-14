# Problem 24/100 — Word Frequency Counter

# Problem Statement:
# User se ek sentence input lo.
# Program ko sentence ke har word ki frequency count karni hai.

# Example 1
# Input:
# Enter a sentence:
# python is easy and python is powerful

# Output:
# python : 2
# is : 2
# easy : 1
# and : 1
# powerful : 1

# Example 2
# Input:
# apple banana apple mango banana apple

# Output:
# apple : 3
# banana : 2
# mango : 1

# Rules:
# 1. Dictionary use karni hai.
# 2. split() use karna hai.
# 3. count() use nahi karna.
# 4. collections.Counter use nahi karna.
# 5. Program case-sensitive reh sakta hai (Bonus baad mein karenge).

# Expected Concepts:
# - String
# - split()
# - Dictionary
# - Loop
# - if-else

# Bonus (Optional):
# Agar input ho:
# Python python PYTHON
#
# Output:
# python : 3
#
# (Hint: String method ka use karna padega.)

sentence = input("Enter a sentence:").lower().split()
frequancy = {}
for i in sentence:
    if i in frequancy:
        frequancy[i]+=1
    else:
        frequancy[i]=1
for key in frequancy:
    print(key,":",frequancy[key])