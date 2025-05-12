# Assignment 3, Task 6
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.2 hrs
# Use of AI: NO
# AI usage details: <DETAILS>

### Your code start here ######
def nycHour(bkkHour: int) -> str:
    nyc_hour = bkkHour - 11
    if nyc_hour <= 0:
        nyc_hour += 24

    prefix = 'am'
    # BKK 11.00 -> NYC 00.00 -> NYC 12am
    if nyc_hour == 0:
        nyc_hour = 12
        prefix = 'am'
    elif nyc_hour < 12:
        prefix = 'am'
    elif nyc_hour == 12:
        prefix = 'pm'
    else:
        nyc_hour -= 12
        prefix = 'pm'

    return str(nyc_hour) + prefix
