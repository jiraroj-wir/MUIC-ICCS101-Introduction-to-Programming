# Assignment 2, Task 3
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.1 hrs
# Use of AI: NO
# AI usage details: <DETAILS>

### Your code start here ######
st = input()
k = int(input())

st_length = len(st)
k %= st_length
print(st[st_length - k:] + st[:st_length - k])
