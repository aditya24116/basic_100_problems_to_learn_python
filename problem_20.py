# Problem 20/100 — First Non-Repeating Character

# Input:
#     programming
    
# Output:
#     First Non-Repeating Character: p

# Explanation:
# p → 1 ✅
# r → 2 ❌
# o → 1 ✅
# g → 2 ❌
# a → 1 ✅
# m → 2 ❌
# i → 1 ✅
# n → 1 ✅

# The first character with frequency 1 is p.

# Rules

# * ✅ Use a dictionary.
# * ❌ Don’t use count().
# * ❌ Don’t use set().
# * Use two loops:
#     1. Create the frequency dictionary.
#     2. Traverse the original string and print the first character whose frequency is 1.

word = input("Enter a word: ")
freq_dict = {}
for i in word:
    if i in freq_dict:
        freq_dict[i]+=1
    else:
        freq_dict[i]=1
for key in word:
    if freq_dict[key]==1:
        print("First Non-Repeating Character:",key)
        break