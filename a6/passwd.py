# Assignment 6, Task 2
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.2 hrs
# Use of AI: NO
# AI usage details: <DETAILS>


### Your code start here ######
def passwordOK(password: str) -> bool:
    lower = False
    numerical = False
    upper = False
    special = False
    triplicates = False

    if len(password) <= 6 or len(password) >= 12:
        return False

    for idx in range(len(password)):
        if password[idx].islower():
            lower = True

        if password[idx] in "0123456789":
            numerical = True

        if password[idx].isupper():
            upper = True

        if password[idx] in "$#@%!":
            special = True

        if idx <= len(password) - 3:
            if password[idx] == password[idx + 1] == password[idx + 2]:
                triplicates = True

    return lower and numerical and upper and special and (not triplicates)


assert passwordOK("ABd1234@1") == True
assert passwordOK("f#9") == False
assert passwordOK("Abbbc1!f") == False
