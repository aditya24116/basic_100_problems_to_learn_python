# Problem 15/100 — Longest Word Finder

# User se ek sentence input lo.

# Example:
#     Python is an amazing programming language
    
# Output:
#     Longest word: programming
#     Length: 11
    
# Rules

# * split() use karo.
# * max() use nahi karna.
# * Loop use karke longest word find karo.

thoughts = input("Enter your message:")
parts = thoughts.split()
length = 0
for i in parts:
    if len(i)>length:
        length=len(i)
        longest_word=i
print("Longest word:",longest_word)
print("Length:",length)