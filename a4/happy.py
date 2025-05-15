# Assignment 4, Task 6
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.2 hrs
# Use of AI: NO
# AI usage details: <DETAILS>


### Your code start here ######
UNIT_SQUARE = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


def sumOfDigitsSquared(n: int) -> int:
    sum = 0
    while n > 0:
        unit = n % 10
        n //= 10

        sum += UNIT_SQUARE[unit]

    return sum


def isHappy(n: int) -> bool:
    while True:
        n = sumOfDigitsSquared(n)
        if n == 1:
            return True
        elif n == 4:
            return False


def kThHappy(k: int) -> int:
    count = 0
    number = 1
    while True:
        if isHappy(number):
            count += 1

        if count == k:
            return number

        number += 1
