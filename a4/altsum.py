# Assignment 4, Task 1
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.1 hrs
# Use of AI: NO
# AI usage details: <DETAILS>


### Your code start here ######
def altSum(lst: list[int]) -> int:
    if len(lst) == 0:
        return 0

    sum: int = lst[0]
    flag = True

    for num in lst[1:]:
        temp = num
        if flag == False:
            temp *= -1
            flag = True
        else:
            flag = not flag

        sum += temp

    return sum
