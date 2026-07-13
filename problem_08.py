# Problem 8/100 — Salary Calculator

# User se basic salary input lo. Calculate karo:

# * HRA = basic salary ka 20%
# * DA = basic salary ka 10%
# * Tax = basic salary ka 5%
# * Final salary = Basic + HRA + DA − Tax

# Output mein Basic Salary, HRA, DA, Tax aur Final Salary sab print karo.

basic_salary = float(input("Enter your basic salary:"))
hra = basic_salary*(20/100)
da = basic_salary*(10/100)
tax = basic_salary*(5/100)
final_salary = basic_salary+hra+da-tax
print("Basic Salary: ",basic_salary)
print("HRA: ",hra)
print("DA: ",da)
print("TAX: ",tax)
print("Final Salary: ",final_salary)