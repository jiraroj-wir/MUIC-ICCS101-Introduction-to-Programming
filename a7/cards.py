# Assignment 7, Task 2
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.3 hrs
# Use of AI: NO
# AI usage details: <DETAILS>


### Your code start here ######
# near the top of the file but above all the functions
Hand = set[tuple[str, str]]

stright_flush_map = {
    "A": 2,
    "2": 3,
    "3": 5,
    "4": 7,
    "5": 11,
    "6": 13,
    "7": 17,
    "8": 19,
    "9": 23,
    "10": 29,
    "J": 31,
    "Q": 37,
    "K": 41,
}


def is_straight_flush(h: Hand) -> bool:
    suit = set()
    rank = set()
    for s, r in h:
        suit.add(s)
        rank.add(r)

    if len(suit) != 1:
        return False

    hash_product = 1
    for r in rank:
        hash_product *= stright_flush_map[r]

    rank_order = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    window = 1

    for i in range(len(rank_order) - 4):
        if i == 0:
            for j in range(5):
                window *= stright_flush_map[rank_order[j]]
        else:
            window //= stright_flush_map[rank_order[i - 1]]
            window *= stright_flush_map[rank_order[i + 4]]

        if window == hash_product:
            return True

    return False


hand_1 = {
    ("Spades", "5"),
    ("Spades", "4"),
    ("Spades", "3"),
    ("Spades", "2"),
    ("Spades", "A"),
}
assert (is_straight_flush(hand_1)) == True

hand_2 = {
    ("Hearts", "A"),
    ("Hearts", "K"),
    ("Hearts", "Q"),
    ("Hearts", "J"),
    ("Hearts", "10"),
}
assert (is_straight_flush(hand_2)) == True

hand_3 = {
    ("Hearts", "10"),
    ("Hearts", "9"),
    ("Hearts", "8"),
    ("Hearts", "7"),
    ("Hearts", "6"),
}
assert (is_straight_flush(hand_3)) == True


def is_four_of_a_kind(h: Hand):
    for s1, r1 in h:
        temp = set()
        temp.add(s1)
        for s2, r2 in h:
            if r2 == r1:
                temp.add(s2)

        if len(temp) == 4:
            return True

    return False


hand_4 = {
    ("Clubs", "3"),
    ("Spades", "3"),
    ("Diamonds", "3"),
    ("Hearts", "3"),
    ("Hearts", "J"),
}

assert is_four_of_a_kind(hand_4) == True
