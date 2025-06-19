# Assignment 6, Task 3
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.3 hrs
# Use of AI: NO
# AI usage details: <DETAILS>


### Your code start here ######
def keepTabs(actions: list[str]) -> dict[str, int]:
    records = {}
    for action in actions:
        if "++" in action:
            person = action[:-2]
            if person not in records:
                records[person] = 0

            records[person] += 1
        elif "--" in action:
            person = action[:-2]
            if person not in records:
                records[person] = 0

            records[person] -= 1
        else:  # i miss elixir pattern matching T_T
            parse_here = -1
            for idx in range(len(action) - 1):
                if action[idx] == "-" and action[idx + 1] == ">":
                    parse_here = idx
                    break

            if parse_here != -1:
                doner = action[:parse_here]
                receiver = action[parse_here + 2 :]

                if doner in records:
                    if receiver not in records:
                        records[receiver] = 0

                    records[receiver] += records[doner]
                    records[doner] = 0

    to_delete = []
    for key, val in records.items():
        if val == 0:
            to_delete.append(key)

    for key in to_delete:
        records.pop(key)

    return records


actions = [
    "Jim++",
    "John--",
    "Jeff++",
    "Jim++",
    "John--",
    "John->Jeff",
    "Jeff--",
    "June++",
    "Home->House",
]

print(keepTabs(actions))
# assert keepTabs(actions) == {"Jeff": -2, "June": 1, "Jim": 2}
