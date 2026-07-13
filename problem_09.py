# Problem 9/100 — Simple Loan EMI Calculator

# User se 3 inputs lo: loan amount, annual interest rate, aur loan duration in years.

# Abhi real bank EMI formula use nahi karna. Simplified calculation karo:

# Total Interest = Loan Amount × Interest Rate × Years / 100
# Total Payment = Loan Amount + Total Interest
# Number of Months = Years × 12
# Monthly Payment = Total Payment / Number of Months

# Example: Loan = ₹100,000, Rate = 10%, Years = 2 → Interest ₹20,000, Total ₹120,000, Monthly Payment ₹5,000.

# Output mein total interest, total payment aur monthly payment print karo.

loan_amount = float(input("Enter your loan amount: "))
annual_interest_rate = float(input("Enter your annual interest rate: "))
loan_duration = float(input("Enter your loan duration: "))
total_interest = loan_amount*annual_interest_rate*loan_duration/100
total_payment = loan_amount+total_interest
monthly_payment = total_payment/(loan_duration*12)
print("Total Payment: ",total_payment)
print("Total Interest: ",total_interest)
print("Monthly Payment: ",monthly_payment)
