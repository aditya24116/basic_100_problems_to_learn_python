# Problem 16/100 — Character Frequency Counter

# Input:
#     programming
    
# Output:
# p : 1
# r : 2
# o : 1
# g : 2
# a : 1
# m : 2
# i : 1
# n : 1

# Rules

# * Dictionary use karni hai.
# * count() method use nahi karna.
# * Har character kitni baar aaya hai, calculate karo.

word = input("Enter a word:")
freq = {}
for i in word:
    if i in freq:
        freq[i]+= 1
    else:
        freq[i]=1
for key in freq:
    print(key,":",freq[key])
    
        
    
    
    