def winner(records: list[dict[str, int]]) -> str:
    map = {}
    for record in records:
        for key in record:
            if record[key] > 1:
                if key not in map:
                    map[key] = 0
                map[key] += 1

    # try sorting map's value with lambda
    sorted_map = sorted(map.items(), key=lambda kv: kv[1], reverse=True)

    if len(sorted_map) == 1:
        return sorted_map[0][0]

    if sorted_map[0][1] == sorted_map[1][1]:
        return ""

    return sorted_map[0][0]


# Chess
assert winner([{"A": 2, "B": 1}]) == "A"
assert winner([{"A": 3, "B": 0}, {"A": 1, "C": 2}]) == ""
assert winner([{"A": 3, "B": 0}, {"A": 1, "C": 2}, {"B": 0, "C": 3}]) == "C"
assert (
    winner([{"A": 3, "B": 0}, {"A": 1, "C": 2}, {"B": 0, "D": 3}, {"A": 2, "D": 1}])
    == "A"
)
assert (
    winner([{"A": 3, "B": 0}, {"B": 2, "C": 1}, {"C": 2, "D": 1}, {"A": 0, "D": 3}])
    == ""
)
