# Assignment 1, Task 5
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.1 hrs
# Use of AI: NO
# AI usage details: <DETAILS>

### Your code start here ######

# Step 1: Read p and q from the console
p = float(input())
q = float(input())

# Step 2: Compute the area
PI = 3.14
π = PI

area_2 = p * q
# area_1 and area_3 can be merged into a circle with radius q/2
radius = q / 2
circle = π * pow(radius, 2)

total_area = area_2 + circle

# Step 3: Print out the result
print("The total area is", total_area)
