# Assignment 4, Task 2
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.1 hrs
# Use of AI: NO
# AI usage details: <DETAILS>


### Your code start here ######
def powerLoop(upto: int) -> None:
    value = 1
    for i in range(upto + 1):
        print(i, value)
        value = (value * 7) % 97
