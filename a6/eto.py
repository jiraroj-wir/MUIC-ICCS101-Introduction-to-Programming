# Assignment 6, Task 4
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.2 hrs
# Use of AI: NO
# AI usage details: <DETAILS>


### Your code start here ######
def eto(lst: list[int]) -> list[int]:
    if len(lst) == 0:
        return []
    head = lst[0]
    tail = lst[1:]

    if (head & 1) == 0:
        return [head] + eto(tail)
    else:
        return eto(tail) + [head]

