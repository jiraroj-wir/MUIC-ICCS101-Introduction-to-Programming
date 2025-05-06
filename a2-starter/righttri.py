# Assignment 2, Task 7
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.1 hrs
# Use of AI: NO
# AI usage details: <DETAILS>

### Your code start here ######
T: float = float(1e-7)

x: float = float(input())
y: float = float(input())
z: float = float(input())
max_float = max(x, y, z)
sum = pow(x, 2) + pow(y, 2) + pow(z, 2)
# print(2 * pow(max_float, 2) == sum)
print(2 * pow(max_float, 2) - sum < T)  # best practice, according to the floating point warning
