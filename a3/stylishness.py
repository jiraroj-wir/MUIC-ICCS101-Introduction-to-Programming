# Assignment 3, Task 7
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.1 hrs
# Use of AI: NO
# AI usage details: <DETAILS>

### Your code start here ######
def got_table(you: int, date: int) -> str:
    if you <= 2 or date <= 2:
        return 'no'
    elif you >= 8 or date >= 8:
        return 'yes'
    else:
        return 'maybe'
