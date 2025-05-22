def create_schedule(nap_slots: list[int], engagements: list[str]) -> list[str]:
    length = len(nap_slots) + len(engagements)
    schedule = [""] * length

    for idx in nap_slots:
        schedule[idx] = "*Nap*"

    for idx in range(length):
        if schedule[idx] == "*Nap*":
            continue

        temp = engagements.pop(0)
        schedule[idx] = temp

    return schedule


assert create_schedule([2], ["Fufu", "Tofu", "Snofu"]) == [
    "Fufu",
    "Tofu",
    "*Nap*",
    "Snofu",
]
assert create_schedule([0, 3, 4], ["S", "E", "S", "A", "M", "E"]) == [
    "*Nap*",
    "S",
    "E",
    "*Nap*",
    "*Nap*",
    "S",
    "A",
    "M",
    "E",
]
assert create_schedule([0, 7], ["P", "y", "T", "h", "o", "n"]) == [
    "*Nap*",
    "P",
    "y",
    "T",
    "h",
    "o",
    "n",
    "*Nap*",
]
assert create_schedule([1, 5, 6], ["F", "I", "S", "H"]) == [
    "F",
    "*Nap*",
    "I",
    "S",
    "H",
    "*Nap*",
    "*Nap*",
]
