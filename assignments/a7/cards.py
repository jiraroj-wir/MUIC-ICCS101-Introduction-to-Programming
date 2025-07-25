# Assignment 7, Task 2
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 4 hrs
# Use of AI: YES
# AI usage details: Fix some typo, clarify the time complexity and emotional support


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

        # this is equivalent to another 4 loops anyway, whats the point?
        # I bet this is even slower than 5 layers of for loop
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


# comment this out for submission, this took 6 seconds
# assert len(all_hands()) == 2598960

"""I dont know whether the assignment wanted a new solution for all_straight_flush(), 
all_four_of_a_kind(), all_full_house() and all_two_pair(); or just use the existing functions. 
I'll do both.

if use the existing functions; running all the functions will takes over 90 seconds
"""


"""
def all_straight_flush() -> list[Hand]:
    hands = all_hands()
    all_possible_stright_flush = []
    for mem in hands:
        if is_straight_flush(mem):
            all_possible_stright_flush.append(mem)

    return all_possible_stright_flush
"""


def all_straight_flush() -> list[Hand]:
    suit_list = ["Club", "Diamond", "Heart", "Spade"]
    rank_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    all_possible_stright_flush = []
    for idx in range(len(rank_list) - 4):
        for suit in suit_list:
            all_possible_stright_flush.append(
                {
                    (suit, rank_list[idx]),
                    (suit, rank_list[idx + 1]),
                    (suit, rank_list[idx + 2]),
                    (suit, rank_list[idx + 3]),
                    (suit, rank_list[idx + 4]),
                }
            )
    return all_possible_stright_flush


assert len(all_straight_flush()) == 40


"""
def all_four_of_a_kind() -> list[Hand]:
    hands = all_hands()
    all_possible_four_of_a_kind = []
    for mem in hands:
        if is_four_of_a_kind(mem):
            all_possible_four_of_a_kind.append(mem)

    return all_possible_four_of_a_kind
"""


def all_four_of_a_kind() -> list[Hand]:
    suit_list = ["Club", "Diamond", "Heart", "Spade"]
    rank_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    deck = []
    for suit in suit_list:
        for rank in rank_list:
            deck.append((suit, rank))

    all_possible_four_of_a_kind = []
    for rank in rank_list:
        for mem in deck:
            if mem[1] != rank:
                all_possible_four_of_a_kind.append(
                    {
                        (suit_list[0], rank),
                        (suit_list[1], rank),
                        (suit_list[2], rank),
                        (suit_list[3], rank),
                        mem,
                    }
                )

    return all_possible_four_of_a_kind


assert len(all_four_of_a_kind()) == 624


"""
def all_full_hose() -> list[Hand]:
    hands = all_hands()
    all_possible_full_house = []
    for mem in hands:
        if is_full_house(mem):
            all_possible_full_house.append(mem)

    return all_possible_full_house
"""


def all_full_house() -> list[Hand]:
    suit_list = ["Club", "Diamond", "Heart", "Spade"]
    rank_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # combination of suit: C(4, 3)
    # small list -- precompute, is this allowed?
    c_4_3 = [
        ["Club", "Diamond", "Heart"],
        ["Club", "Diamond", "Spade"],
        ["Club", "Heart", "Spade"],
        ["Diamond", "Heart", "Spade"],
    ]
    # combination of suit: C(4, 2)
    c_4_2 = []
    for i in range(len(suit_list)):
        for j in range(i + 1, len(suit_list)):
            c_4_2.append([suit_list[i], suit_list[j]])

    all_possible_full_house = []
    for r1_idx in range(len(rank_list)):
        for r2_idx in range(len(rank_list)):
            if r1_idx == r2_idx:
                continue

            for three_of_a_kind in c_4_3:
                hand = []
                for suit in three_of_a_kind:
                    hand.append((suit, rank_list[r1_idx]))

                for pair in c_4_2:
                    full_hand = set()
                    for card in hand:
                        full_hand.add(card)
                    full_hand.add((pair[0], rank_list[r2_idx]))
                    full_hand.add((pair[1], rank_list[r2_idx]))
                    all_possible_full_house.append(full_hand)

    return all_possible_full_house


assert len(all_full_house()) == 3744


"""
def all_two_pair() -> list[Hand]:
    hands = all_hands()
    all_possible_two_pair = []
    for mem in hands:
        if is_two_pair(mem):
            all_possible_two_pair.append(mem)

    return all_possible_two_pair
"""


def all_two_pair() -> list[Hand]:
    suit_list = ["Club", "Diamond", "Heart", "Spade"]
    rank_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    deck = []
    for suit in suit_list:
        for rank in rank_list:
            deck.append((suit, rank))

    # combination of suit: C(4, 3)
    # small list -- precompute, is this allowed?
    """
    c_4_3 = [
        ["Club", "Diamond", "Heart"],
        ["Club", "Diamond", "Spade"],
        ["Club", "Heart", "Spade"],
        ["Diamond", "Heart", "Spade"],
    ]
    """
    # combination of suit: C(4, 2)
    c_4_2 = []
    for i in range(len(suit_list)):
        for j in range(i + 1, len(suit_list)):
            c_4_2.append([suit_list[i], suit_list[j]])

    all_possible_two_pair = []
    for r1_idx in range(len(rank_list)):
        for r2_idx in range(r1_idx + 1, len(rank_list)):
            for pair_1 in c_4_2:
                hand_1 = []
                for suit in pair_1:
                    hand_1.append((suit, rank_list[r1_idx]))

                for pair_2 in c_4_2:
                    hand_2 = set()
                    for clone_1 in hand_1:
                        hand_2.add(clone_1)
                    hand_2.add((pair_2[0], rank_list[r2_idx]))
                    hand_2.add((pair_2[1], rank_list[r2_idx]))

                    for card in deck:
                        if card[1] == rank_list[r1_idx] or card[1] == rank_list[r2_idx]:
                            continue

                        full_hand = set()
                        for clone_2 in hand_2:
                            full_hand.add(clone_2)
                        full_hand.add(card)

                        all_possible_two_pair.append(full_hand)

    return all_possible_two_pair


assert len(all_two_pair()) == 123552
