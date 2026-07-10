# Problem 11/100 — Palindrome Checker

# User se ek word input lo aur check karo ki word palindrome hai ya nahi.

# madam → Palindrome
# level → Palindrome
# python → Not Palindrome

word = input("Enter a word: ")
reversed_word = ""
for i in word:
    reversed_word = i+reversed_word
if word == reversed_word:
    print("Palindrome")
else:
    print("Not Palindrome")
    