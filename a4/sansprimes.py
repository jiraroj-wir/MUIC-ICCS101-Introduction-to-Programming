# Assignment 4, Task 7
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.2 hrs
# Use of AI: NO
# AI usage details: <DETAILS>


### Your code start here ######
import math


def is_prime(n: int) -> bool:
    num = 2
    if n < 2:
        return False

    while num <= math.sqrt(n):
        if n % num == 0:
            return False

        num += 1

    return True


def sans_primes(numbers: list[int]) -> list[int]:
    new_list: list[int] = []
    length = len(numbers)
    idx = 0
    while idx < length:
        temp = numbers[idx]

        if is_prime(temp):
            print(temp)
            idx += 2
            continue

        new_list.append(temp)
        idx += 1

    return new_list
