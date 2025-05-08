# Assignment 3, Task 6
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.1 hrs
# Use of AI: NO
# AI usage details: <DETAILS>

### Your code start here ######
def nycHour(bkkHour: int) -> str:
    nyc_hour = bkkHour - 11
    if nyc_hour <= 0:
        nyc_hour += 24

    prefix = 'am'
    if nyc_hour > 12:
        prefix = 'pm'
        nyc_hour -= 12

    return str(nyc_hour) + prefix
