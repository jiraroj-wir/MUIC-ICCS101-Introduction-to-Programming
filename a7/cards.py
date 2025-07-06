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
    rank_map = {}
    for _s, r in h:
        if r not in rank_map:
            rank_map[r] = 1
        else:
            rank_map[r] += 1

        if rank_map[r] == 4:
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


# there shouldn't be repeated cards on the same deck -- a set of 5 cards?
def is_full_house(h: Hand) -> bool:
    rank_map = {}
    for _s, r in h:
        if r not in rank_map:
            rank_map[r] = 1
        else:
            rank_map[r] += 1

    got_triple = False
    got_pair = False
    for key in rank_map:
        val = rank_map[key]
        if val == 3:
            got_triple = True

        if val == 2:
            got_pair = True

    return got_triple and got_pair


hand_5 = {
    ("Clubs", "4"),
    ("Spades", "4"),
    ("Diamonds", "4"),
    ("Hearts", "7"),
    ("Spades", "7"),
}
assert is_full_house(hand_5) == True


def is_two_pair(h: Hand) -> bool:
    rank_map = {}
    for _s, r in h:
        if r not in rank_map:
            rank_map[r] = 1
        else:
            rank_map[r] += 1

    pair_count = 0
    for key in rank_map:
        val = rank_map[key]

        if val == 2:
            pair_count += 1

    return pair_count == 2


hand_6 = {
    ("Hearts", "9"),
    ("Clubs", "9"),
    ("Spades", "4"),
    ("Clubs", "4"),
    ("Clubs", "10"),
}
assert is_two_pair(hand_6) == True


# does time complexity even matter here? We have to go through at least C(52, 5) anyway?
def all_hands() -> list[Hand]:
    suit_list = ["Club", "Diamond", "Heart", "Spade"]
    rank_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    deck = []
    for suit in suit_list:
        for rank in rank_list:
            deck.append((suit, rank))

    deck_len = len(deck)  # 52
    all = []
    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    while a <= deck_len - 5:
        hand = {deck[a], deck[b], deck[c], deck[d], deck[e]}

        all.append(hand)

        e += 1
        if e >= deck_len:
            d += 1
            if d >= deck_len - 1:
                c += 1
                if c >= deck_len - 2:
                    b += 1
                    if b >= deck_len - 3:
                        a += 1
                        b = a + 1
                    c = b + 1
                d = c + 1
            e = d + 1

    return all


assert len(all_hands()) == 2598960

"""I dont know whether the assignment wanted a new solution for all_straight_flush(), 
all_four_of_a_kind(), all_full_house() and all_two_pair(); or just use the existing functions. 
I'll do both.
"""


def all_straight_flush() -> list[Hand]:
    hands = all_hands()
    all_possible_stright_flush = []
    for mem in hands:
        if is_straight_flush(mem):
            all_possible_stright_flush.append(mem)

    print(len(all_possible_stright_flush))
    return all_possible_stright_flush


assert len(all_straight_flush()) == 40
