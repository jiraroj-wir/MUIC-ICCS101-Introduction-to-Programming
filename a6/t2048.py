# Assignment 6, Task 6
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 4:00 hrs
# Use of AI: NO
# AI usage details: <DETAILS>
# ----------------------------------

"""for macos-arm64 user
if your python or the venv is missing `_tkinter` -- should show sth like this:


File "/opt/homebrew/Cellar/python@3.13/3.13.3/Frameworks/Python.framework/Versions/3.13/lib/python3.13/tkinter/__init__.py", line 38, in <module>
    import _tkinter # If this fails your Python may not be configured for Tk
    ^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named '_tkinter'


I supposed that means, you install python via homebrew, and homebrew doesn't have Tk support.
Thus, you need to install tk for python separately via `brew install python-tk`
"""

### Your code start here ######
from typing import List, Tuple

Board = List[List[str]]

# Checks whether a given board has any
# possible move left. If no more moves,
# return True. Otherwise return False.

DIRECTION = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1),
}


# https://www.geeksforgeeks.org/matrix-transpose-without-numpy-in-python/
def transpose(board: Board) -> Board:
    return [list(row) for row in zip(*board)]


# horizontal reflection
def mirror(board: Board) -> Board:
    reflection = []
    for row in board:
        new_row = row[:]
        new_row.reverse()
        reflection.append(new_row)
    return reflection


def isGameOver(board: Board) -> bool:
    if emptyPos(board):
        return False

    change_U, _board = doKeyUp(board)
    change_D, _board = doKeyDown(board)
    change_R, _board = doKeyRight(board)
    change_L, _board = doKeyLeft(board)

    return not (change_U or change_D or change_R or change_L)


# Returns a tuple (changed, new_board)
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Up' key.


def doKeyUp(board: Board) -> Tuple[bool, Board]:
    board = mirror(transpose(board))
    [changed, new_board] = doKeyRight(board)
    new_board = transpose(mirror(new_board))

    return changed, new_board


# Returns a tuple (changed, new_board)
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Down' key.


def doKeyDown(board: Board) -> Tuple[bool, Board]:
    board = transpose(board)
    [changed, new_board] = doKeyRight(board)
    new_board = transpose(new_board)

    return changed, new_board


# Returns a tuple (changed, new_board)
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Left' key.


def doKeyLeft(board: Board) -> Tuple[bool, Board]:
    reflection = mirror(board)
    [changed, new_board] = doKeyRight(reflection)
    new_board = mirror(new_board)

    return changed, new_board


# Returns a tuple (changed, new_board)
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Right' key.
#
# This is so ugly, I can't make it better -- sadly
def doKeyRight(board: Board) -> Tuple[bool, Board]:
    new_board = []
    changed = False
    for row in board:
        # STEP 1: Slide in the Direction of Movement
        new_row = []
        temp = []
        for mem in row:
            if mem == " ":
                temp.append(" ")
                continue
            new_row.append(mem)

        new_row = temp + new_row

        # STEP 2: Compact Similar Blocks
        idx = len(new_row) - 1
        while idx > 0:
            if new_row[idx] != " " and new_row[idx] == new_row[idx - 1]:
                new_row[idx] = str(int(new_row[idx]) + int(new_row[idx - 1]))
                new_row[idx - 1] = " "
                idx -= 1
            idx -= 1

        # STEP 3: Slide Once More
        new_new_row = []
        temp = []
        for mem in new_row:
            if mem == " ":
                temp.append(" ")
                continue
            new_new_row.append(mem)

        new_new_row = temp + new_new_row

        new_board.append(new_new_row)

        if new_new_row != row:
            changed = True

    return changed, new_board


# Returns a list of tuples (row, col)
# indicating where the empty spots are
def emptyPos(board: Board) -> List[Tuple[int, int]]:
    empty_position = []
    for idx_i in range(len(board)):
        for idx_j in range(len(board[idx_i])):
            if board[idx_i][idx_j] == " ":
                empty_position.append((idx_i, idx_j))

    return empty_position
