# Assignment 3, Task 1
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.1 hrs
# Use of AI: NO
# AI usage details: <DETAILS>

### Your code start here ######
import sys

def my_min(p: float, q: float, r: float) -> float:
    min_float = sys.float_info.max
    if p < min_float:
        min_float = p
    if q < min_float:
        min_float = q
    if r < min_float:
        min_float = r

    return min_float

def my_max(p: float, q: float, r: float) -> float:
    max_float = sys.float_info.min
    if p > max_float:
        max_float = p
    if q > max_float:
        max_float = q
    if r > max_float:
        max_float = r

    return max_float



def my_mean(p: float, q: float, r: float) -> float:
    sum = p + q + r

    return sum / 3.0


def my_med(p: float, q: float, r: float) -> float:
    sum = p + q + r
    min_float = my_min(p, q, r)
    max_float = my_max(p, q, r)

    return sum - min_float - max_float
