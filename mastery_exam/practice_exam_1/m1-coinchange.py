def coinChange(v: int) -> list[int]:
    change = []
    while v > 0:
        if v // 10 > 0:
            v -= 10
            change.append(10)
        elif v // 5 > 0:
            v -= 5
            change.append(5)
        elif v // 2 > 0:
            v -= 2
            change.append(2)
        else:
            v -= 1
            change.append(1)

    return change


assert coinChange(38) == [10, 10, 10, 5, 2, 1]
assert coinChange(19) == [10, 5, 2, 2]
assert coinChange(11) == [10, 1]
assert coinChange(5) == [5]
assert coinChange(3) == [2, 1]
