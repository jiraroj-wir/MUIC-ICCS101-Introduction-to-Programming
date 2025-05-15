# Assignment 4, Task 3
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.1 hrs
# Use of AI: NO
# AI usage details: <DETAILS>


### Your code start here ######
def triangle(k: int) -> None:
    width = 2 * k - 1
    for i in range(k):
        temp: str = ""
        star_size = i * 2 + 1
        square_size = (width - star_size) // 2
        temp += "#" * square_size
        temp += "*" * star_size
        temp += "#" * square_size

        print(temp)


def diamond(k: int) -> None:
    # too lazy, just copy triangle fn and tweak stuff
    k += 1
    width = 2 * k - 1
    for i in range(k - 1):
        temp: str = ""
        star_size = i * 2 + 1
        square_size = (width - star_size) // 2
        temp += "#" * square_size
        temp += "*" * star_size
        temp += "#" * square_size

        print(temp)

    for j in range(k - 1):
        j = k - j - 2
        temp: str = ""
        star_size = j * 2 + 1
        square_size = (width - star_size) // 2
        temp += "#" * square_size
        temp += "*" * star_size
        temp += "#" * square_size

        print(temp)
