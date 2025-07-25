# Assignment 4, Task 4
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.2 hrs
# Use of AI: NO
# AI usage details: <DETAILS>


### Your code start here ######
def readAloud(lst: list[int]) -> list[int]:
    length = len(lst)
    read_aloud: list[int] = []
    temp = lst[0]
    count = 1
    for idx in range(1, length):
        if lst[idx] == temp:
            count += 1
            continue

        read_aloud.append(count)
        read_aloud.append(temp)
        temp = lst[idx]
        count = 1

    read_aloud.append(count)
    read_aloud.append(temp)

    return read_aloud
