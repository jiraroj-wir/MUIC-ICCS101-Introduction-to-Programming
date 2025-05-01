# Assignment 2, Task 5
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.1 hrs
# Use of AI: NO
# AI usage details: <DETAILS>

### Your code start here ######
p: int = int(input())
q: int = int(input())
r: int = int(input())
s: int = int(input())

max_num = max(p, q, r, s)
min_num = min(p, q, r, s)
sum = p + q + r + s
print((sum - max_num - min_num)/2)
