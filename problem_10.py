# Problem 10/100 — Shopping Discount Calculator

# Total shopping amount input lo aur discount slabs apply karo:

# * Less than ₹1,000 → 0%
# * ₹1,000 to ₹4,999 → 5%
# * ₹5,000 to ₹9,999 → 10%
# * ₹10,000 or more → 20%

# Print karo: Original Amount, Discount Amount, aur Final Payable Amount.

total_shopping_amount = float(input("Enter your Total shopping amount: "))
discount_amount = 0
if total_shopping_amount<1000:
    discount_amount = 0
elif total_shopping_amount<=4999:
    discount_amount = total_shopping_amount*0.05
elif total_shopping_amount<=9999:
    discount_amount = total_shopping_amount*0.1
elif total_shopping_amount>=10000:
    discount_amount = total_shopping_amount*0.2

print("Orignal Amount: ",total_shopping_amount)
print("Discount Amount: ",discount_amount)
print("Final Payable Amount: ",total_shopping_amount-discount_amount)
