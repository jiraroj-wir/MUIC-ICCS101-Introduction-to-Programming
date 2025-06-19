# Assignment 6, Task 1
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 1 hrs
# Use of AI: YES
# AI usage details: Lambda function in python


### Your code start here ######
def charHistogram(filename: str) -> None:
    word_map = {}
    with open(filename, "r") as f:
        while True:
            char = f.read(1)
            if not char:
                break

            char = char.lower()
            if not char.isalpha():
                continue

            if char not in word_map:
                word_map[char] = 1
                continue

            word_map[char] += 1

    word_map = dict(sorted(word_map.items(), key=lambda item: (-item[1], item[0])))
    for ch, val in word_map.items():
        print(ch, "+" * val)
