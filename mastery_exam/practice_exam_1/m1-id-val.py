def valid_id(idnum: str) -> bool:
    c = 0

    for idx in range(15 - 1):
        c += int(idnum[idx]) * (15 - idx)

    a = (11 - c % 11) % 10

    return int(idnum[14]) == a


assert valid_id("180628621489758") == True
assert valid_id("606228772259487") == False
assert valid_id("729921769655535") == True
assert valid_id("171009540283809") == False
assert valid_id("123045607890126") == True
