# Assignment 5, Task 2
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.2 hrs
# Use of AI: NO
# AI usage details: <DETAILS>


### Your code start here ######
def is_hidden(s, t) -> bool:
    s = s.lower()
    t = t.lower()

    t_idx = 0
    t_length = len(t)
    for ch in s:
        if ch == t[t_idx]:
            t_idx += 1

        if t_idx == t_length:
            return True

    return False


assert is_hidden("welcometothehotelcalifornia", "melon") == True
assert is_hidden("welcometothehotelcalifornia", "space") == False
assert is_hidden("TQ89MnQU3IC7t6", "MUIC") == True
assert is_hidden("VhHTdipc07", "htc") == True
assert is_hidden("VhHTdipc07", "hTc") == True
assert is_hidden("VhHTdipc07", "vat") == False
