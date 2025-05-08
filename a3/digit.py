# Assignment 3, Task 3
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.2 hrs
# Use of AI: NO
# AI usage details: <DETAILS>

### Your code start here ######
def kthDigit(x: int, b: int, k: int) -> int:
    return (x // pow(b, k)) % b

# first approach, with loop
'''
def kthDigit(x: int, b: int, k: int) -> int:
    iter = 0
    while (True):
        mod_product = x % b
        x //= b
        if iter == k:
            return mod_product

        iter += 1
'''
