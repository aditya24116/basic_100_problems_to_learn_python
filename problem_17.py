# Problem 17/100 — Remove Duplicates from a List

# Input:
#     [1, 2, 3, 2, 4, 1, 5, 3]
    
# Output:
#     [1, 2, 3, 4, 5]
    
# Rules

# * ❌ set() use nahi karna.
# * ✅ List aur loop use karna.
# * Original order preserve rehna chahiye.

# Example:
#     Input  : [5, 3, 5, 2, 3, 1]
#     Output : [5, 3, 2, 1]
    

num =  list(map(int,input("Enter Numbers:").split()))
output = []
for i in num:
    if i not in  output:
        output.append(i)
print(output)
# for i in output:
#         count = 0
#         for j in num:
#             if i == j:
#                 count += 1
#         print(i ,"=",count)