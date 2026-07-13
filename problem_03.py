# Problem 3/100 — Restaurant Bill Calculator

# User se 2 inputs lo:

# * Bill amount
# * Tip percentage

# Final amount calculate karo.

# Example: Bill = 1000, Tip = 10% → Tip amount = 100, Final amount = 1100.

# Output mein tip amount aur final payable amount dono print karo.

Bill = float(input("Enter your bill amount: "))
Tip_percentage = float(input("Enter your Tip percentage: "))
Tip_amount = Bill*Tip_percentage/100
Total_payable_amount = Bill+Tip_amount
print("Your bill amount:", Bill)
print("Tip amount: ",Tip_amount)
print("Total payable amount: ",Total_payable_amount)
