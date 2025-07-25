# Assignment 5, Task 6
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.3 hrs
# Use of AI: NO
# AI usage details: <DETAILS>


### Your code start here ######
def separate(data: list[int], k: int) -> list[list[int]]:
    d = []
    for idx in range(len(data) - 1):
        temp = data[idx + 1] - data[idx]
        d.append((temp, idx))

    d = sorted(d, reverse=True)
    split_idx = []
    for idx in range(k - 1):
        split_idx.append(d[idx][1])

    split_idx = sorted(split_idx)

    separated = []
    prev = 0
    for si in split_idx:
        separated.append(data[prev : si + 1])
        prev = si + 1

    separated.append(data[prev:])

    return separated


assert separate([10, 12, 45, 47, 91, 98, 99], 3) == [[10, 12], [45, 47], [91, 98, 99]]
