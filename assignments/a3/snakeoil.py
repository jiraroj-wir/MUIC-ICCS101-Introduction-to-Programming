# Assignment 3, Task 2
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.1 hrs
# Use of AI: NO
# AI usage details: <DETAILS>

### Your code start here ######
def price(vol: int) -> float:
    price = vol * 18.0
    discount = False
    shipping = 0.0
    if vol < 20 and vol > 0:
        shipping = 250
    elif vol > 100:
        discount = True
    else:
        shipping = 10 * vol

    if discount:
        price *= 0.99

    return price + shipping
