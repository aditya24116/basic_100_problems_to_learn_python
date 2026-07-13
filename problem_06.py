# Problem 6/100 — Electricity Bill Calculator ⚡
# Units ke according bill calculate karo:
    
# Units                       Rate

# First 100 units             ₹5/unit

# Next 100 units (101–200)    ₹7/unit

# Above 200                   ₹10/unit
# Example: agar usage 250 units hai, calculation hogi: first 100 = ₹500, next 100 = ₹700, remaining 50 = ₹500, so total bill = ₹1700.

Units = int(input("Enter your units:"))
if Units>200:
    bill = ((Units-200)*10)+1200
elif Units>100:
    bill = ((Units-100)*7)+500
elif Units<=100:
    bill = Units*5
print("Your bill amount is :",bill)
