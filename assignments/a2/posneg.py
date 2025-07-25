# Assignment 2, Task 2
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 1.5 hrs
# Use of AI: NO
# AI usage details: <DETAILS>

### Your code start here ######
a: int = int(input())
b: int = int(input())
negative:bool = input().lower() == 'true'

# why is this question so hard
# I just try feature engineering each of them and got a working ones, requires a lot of observation
print((((a < 0) == (b < 0)) == (a < 0 and b < 0 and negative)) and a != 0 and b != 0)
