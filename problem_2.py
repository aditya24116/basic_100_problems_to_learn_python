# Problem 2/100 — Temperature Converter

# Program banao jo:

# * Celsius input le
# * Fahrenheit calculate kare
# * Result print kare

# Formula:
# Fahrenheit = (Celsius × 9/5) + 32

# Example:
# Enter temperature in Celsius: 25
# Temperature in Fahrenheit: 77.0

Celsius = float(input("Enter your temeprature in celsius: "))
Fahrenheit = (Celsius*9/5)+32
print("Your temperature in Fahrenheit: ",Fahrenheit)

# Second way to solve this problem

# Celsius = float(input("Enter your temeprature in celsius: "))
# print(f"Your temperature in Fahrenheit: ",(Celsius*9/5)+32)