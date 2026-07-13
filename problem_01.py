# Problem 1/100 — Largest & Smallest Number

# User se 3 numbers input lo aur find karo:

# * Largest number
# * Smallest number

# Rules: max() aur min() use nahi karne. if / elif / else use kar sakte ho.

# Example output:
    
#    Enter first number: 12
#    Enter second number: 45
#    Enter third number: 7

#    Largest: 45
#    Smallest: 7
Num1 = int(input("Enter first number: "))
Num2 = int(input("Enter second number: "))
Num3 = int(input("Enter third number: "))
    
if Num1>=Num2 and Num1>=Num3:
    print("Largest Number: ",Num1)
elif Num2>=Num1 and Num2>=Num3:
    print("Largest Number: ",Num2)
else:
    print("Largest Number: ",Num3)

if Num1<=Num2 and Num1<=Num3:
    print("Smallest Number: ",Num1)
elif Num2<=Num1 and Num2<=Num3:
    print("Smallest Number: ",Num2)
else:
    print("Smallest Number: ",Num3)
    
#Second way to solve this problem



'''
N1 = int(input("Enter first number:"))
N2 = int(input("Enter second number:"))
N3 = int(input("Enter third number:"))
l = []
for i in N1,N2,N3:
    l.append(i)
largest = l[0]
smallest = l[0]
for i in l:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i
print("Largest number is =",largest)
print("Smallest number is =",smallest)
'''