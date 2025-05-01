# Assignment 2, Task 6
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.1 hrs
# Use of AI: NO
# AI usage details: <DETAILS>

### Your code start here ######
hour: int = int(input())
minute: int = int(input())
meowing:bool = input().lower() == 'true'
minute_day: int = 60 * hour + minute
print(meowing and (minute_day < 6 * 60 + 30 or minute_day > 21 * 60))
