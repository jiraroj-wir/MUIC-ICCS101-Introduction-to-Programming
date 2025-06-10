# Assignment 5, Task 4
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.3 hrs
# Use of AI: NO
# AI usage details: <DETAILS>


### Your code start here ######
def parse_time(line: str) -> int:
    hours = 0
    minutes = 0
    now_minute = False
    temp = 0

    for ch in line:
        if not ch.isnumeric():
            if ch == ",":
                now_minute = True
                hours = temp
                temp = 0
                continue
            break

        temp = temp * 10 + int(ch)

    if now_minute:
        minutes = hours * 60 + temp
    else:
        minutes = temp * 60

    return minutes


def parse_dist(line: str) -> float:
    line_length = len(line)

    for i in range(line_length):
        idx = line_length - i - 1

        if not line[idx].isnumeric():
            if line[idx] == ".":
                continue

            break

    return float(line[idx + 1 : line_length])


def jogging_average(activities: list[str]) -> float:
    time = 0
    distance = 0

    for log in activities:
        if "jogging;time:" in log:
            time += parse_time(log[13:])
            distance += parse_dist(log[13:])

    return distance * 1000 / time


log_book = [
    "cycling;time:1,49;distance:2",
    "jogging;time:40,11;distance:6",
    "swimming;time:1,49;distance:1.2",
    "jogging;time:36,25;distance:5.3",
    "hiking;time:106,01;distance:8.29",
]

print(jogging_average(log_book))
