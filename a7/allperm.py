# Assignment 7, Task 1
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.3 hrs
# Use of AI: NO
# AI usage details: <DETAILS>


### Your code start here ######
def all_perm(n: int) -> set[tuple[int, ...]]:
    if n == 1:
        return {(1,)}

    perm_set = set()
    for tup in all_perm(n - 1):
        for idx in range(len(tup) + 1):
            perm_set.add(tup[:idx] + (int(n),) + tup[idx:])

    return perm_set


assert all_perm(2) == {(1, 2), (2, 1)}
assert all_perm(3) == {(3, 1, 2), (1, 3, 2), (1, 2, 3), (3, 2, 1), (2, 3, 1), (2, 1, 3)}
assert all_perm(4) == {
    (4, 3, 1, 2),
    (3, 4, 1, 2),
    (3, 1, 4, 2),
    (3, 1, 2, 4),
    (4, 1, 3, 2),
    (1, 4, 3, 2),
    (1, 3, 4, 2),
    (1, 3, 2, 4),
    (4, 1, 2, 3),
    (1, 4, 2, 3),
    (1, 2, 4, 3),
    (1, 2, 3, 4),
    (4, 3, 2, 1),
    (3, 4, 2, 1),
    (3, 2, 4, 1),
    (3, 2, 1, 4),
    (4, 2, 3, 1),
    (2, 4, 3, 1),
    (2, 3, 4, 1),
    (2, 3, 1, 4),
    (4, 2, 1, 3),
    (2, 4, 1, 3),
    (2, 1, 4, 3),
    (2, 1, 3, 4),
}
