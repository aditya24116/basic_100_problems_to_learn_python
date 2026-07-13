# Problem 13/100 — Clean and Format Full Name

# User messy name enter kare, for example:
#        aAdItYa   rAnA
# Program output kare:
#     Aaditya Rana
# Requirements: extra spaces remove karo, multiple spaces ko single space banao, aur har name word ka first letter capital karo.
name = input("Enter your name:")
name = name.strip()
word = name.split()
clean_name = " ".join(word)
clean_name = clean_name.title()
print("Your name is",clean_name)