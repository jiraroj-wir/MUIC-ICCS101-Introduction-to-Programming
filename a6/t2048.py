# Assignment XX, Task YY
# Name: Eye Loveprograming
# Collaborators: John Nonexistent
# Time Spent: 4:00 hrs
# ----------------------------------
from typing import List, Tuple

Board = List[List[str]]

# Checks whether a given board has any
# possible move left. If no more moves,
# return True. Otherwise return False.


def isGameOver(board: Board) -> bool:
    return False

# Returns a tuple (changed, new_board)
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Up' key.


def doKeyUp(board: Board) -> Tuple[bool, Board]:
    return False, board

# Returns a tuple (changed, new_board)
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Down' key.


def doKeyDown(board: Board) -> Tuple[bool, Board]:
    return False, board

# Returns a tuple (changed, new_board)
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Left' key.


def doKeyLeft(board: Board) -> Tuple[bool, Board]:
    return False, board


# Returns a tuple (changed, new_board)
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Right' key.
def doKeyRight(board: Board) -> Tuple[bool, Board]:
    return False, board


# Returns a list of tuples (row, col)
# indicating where the empty spots are
def emptyPos(board: Board) -> List[Tuple[int, int]]:
    return []
