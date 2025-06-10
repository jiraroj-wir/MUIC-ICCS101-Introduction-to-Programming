# Assignment 5, Task 5
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 1.0 hrs
# Use of AI: NO
# AI usage details: <DETAILS>

"""
partial rabin-karp algorithm, I don't think it gain much speed compare to normal approach, since i didnt implement the rolling hash part.
so, roughly O(75*75) + O(50*150*w); w = average word length, rather than O(50*75*75*w) for brute force, thats 30 times faster right?
"""


### Your code start here ######
# normal prime hash here, not rolling hash
def hash(s: str) -> int:
    char_prime_map = {
        "a": 2,
        "b": 3,
        "c": 5,
        "d": 7,
        "e": 11,
        "f": 13,
        "g": 17,
        "h": 19,
        "i": 23,
        "j": 29,
        "k": 31,
        "l": 37,
        "m": 41,
        "n": 43,
        "o": 47,
        "p": 53,
        "q": 59,
        "r": 61,
        "s": 67,
        "t": 71,
        "u": 73,
        "v": 79,
        "w": 83,
        "x": 89,
        "y": 97,
        "z": 101,
    }
    product = 1
    for ch in s:
        product *= char_prime_map[ch]

    return product


def rabin_karp_on_grid(candidates: list[str], word: str) -> bool:
    word_hash = hash(word)
    for candidate in candidates:
        for i in range(len(candidate) - len(word) + 1):
            temp = hash(candidate[i : i + len(word)])
            if temp == word_hash:
                if (
                    candidate[i : i + len(word)] == word
                ):  # double check, I don't wanna get ghosted by these probabilistic algo.
                    return True
    return False


def make_candidates(grid: list[list[str]]) -> list[str]:
    rows, cols = len(grid), len(grid[0])
    candidates = []

    # left to right
    for r in range(rows):
        line = ""
        for c in range(cols):
            line += grid[r][c]
        candidates.append(line)

    # top to bottom
    for c in range(cols):
        line = ""
        for r in range(rows):
            line += grid[r][c]
        candidates.append(line)

    # top-left to bottom-right
    for d in range(-(rows - 1), cols):
        line = ""
        for r in range(rows):
            c = d + r
            if 0 <= c < cols:
                line += grid[r][c]
        if line:
            candidates.append(line)

    # bottom-left to top-right
    for d in range(rows + cols - 1):
        line = ""
        for r in range(rows):
            c = d - r
            if 0 <= c < cols:
                line += grid[r][c]
        if line:
            candidates.append(line)

    return candidates


# unnecessary, since we use rabin-karp
# def contains_word(grid: list[list[str]], w: str) -> bool t:
# def make_unique(lst: list[str]) -> list[str]:


def word_sleuth(grid: list[list[str]], words: list[str]) -> list[str]:
    in_grid = []
    candidates = make_candidates(grid)
    for word in words:
        if rabin_karp_on_grid(candidates, word):
            in_grid.append(word)

    return in_grid


grid = [
    ["r", "a", "w", "b", "i", "t"],
    ["x", "a", "y", "z", "c", "h"],
    ["p", "q", "b", "e", "i", "e"],
    ["t", "r", "s", "b", "o", "g"],
    ["u", "w", "x", "v", "i", "t"],
    ["n", "m", "r", "w", "o", "t"],
]

words = ["bog", "moon", "rabbit", "the", "bit", "raw"]

# testcase got different output order, so use a set
assert set(word_sleuth(grid, words)) == {"raw", "bit", "rabbit", "bog", "the"}
