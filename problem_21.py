# Problem 21/100 — Anagram Checker

# Problem Statement

# User se 2 words input lo.

# Check karo ki dono words anagrams hain ya nahi.

# Anagram kya hota hai?

# Do words jinke letters same hon, bas order different ho.

# Examples

# listen
# silent
# ✅ Anagram

# heart
# earth
# ✅ Anagram

# python
# java
# ❌ Not Anagram

# Rules

# * ❌ sorted() use nahi karna.
# * ❌ collections.Counter use nahi karna.
# * ✅ Dictionary use karni hai.
# * ✅ Do alag frequency dictionaries banao.
# * Fir dono dictionaries compare karo.
# Input:
#     Enter first word: listen
#     Enter second word: silent
    
# Output:
#     These words are anagrams.

first_word = input("Enter the first word:")
second_word = input("Enter the second word:")
if len(first_word)!=len(second_word):
    print("These words are not anagrams.")
else:
    first_word_dict = {}
    second_word_dict = {}
    for i in first_word:
        if i in first_word_dict:
            first_word_dict[i]+=1
        else:
            first_word_dict[i]=1
    for i in second_word:
        if i in second_word_dict:
            second_word_dict[i]+=1
        else:
            second_word_dict[i]=1
    if first_word_dict == second_word_dict:
        print("These words are anagrams.")
    else:
        print("These words are not anagrams.")