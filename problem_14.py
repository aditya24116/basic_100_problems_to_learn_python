# Problem 14/100 — Email Parser 📧

# User se email input lo.

# Example:
#     aditya.rana2407@gmail.com

# Output:
#     Username: aditya.rana2407
#     Domain: gmail.com

# Rules

# * split() use karo.
# * Sirf valid email assume karo (ek hi @ hoga).
# * find(), slicing ya regex use mat karna. Sirf split() se solve karo.

email = input("Enter your email:")
username,domain = email.split("@")

print("Username:",username)
print("Domain:",domain)