# Assignment 5, Task 3
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.3 hrs
# Use of AI: NO
# AI usage details: <DETAILS>

# O(n) time complexity, nice :)


### Your code start here ######
def enc(msg: str, key: int) -> str:
    grid = []
    msg_len = len(msg)
    encrypted_string = ""
    rows = -(-msg_len // key)

    for i in range(key * rows):
        temp = (i % rows) * key + (i // rows)
        if temp >= msg_len:
            continue

        encrypted_string = encrypted_string + msg[temp]

    return encrypted_string


assert enc("abc", 2) == "acb"
assert enc("monosodium glutamate", 7) == "mitouanmmo asgtoledu"
assert enc("polylogarithmicsubexponential", 3) == "pygimseonaolatiuxntllorhcbpei"
