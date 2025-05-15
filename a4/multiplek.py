# Assignment 4, Task 5
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.1 hrs
# Use of AI: NO
# AI usage details: <DETAILS>


### Your code start here ######
def allMultiplesOfK(k: int, lst: list[int]) -> bool:
    for val in lst:
        if val % k != 0:
            return False

    return True
