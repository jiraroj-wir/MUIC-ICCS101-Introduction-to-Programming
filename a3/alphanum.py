# Assignment 3, Task 5
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.1 hrs
# Use of AI: NO
# AI usage details: <DETAILS>

### Your code start here ######
def helper_function(ch: str) -> int:
    if ch in 'abc':
        return 2
    elif ch in 'def':
        return 3
    elif ch in 'ghi':
        return 4
    elif ch in 'jkl':
        return 5
    elif ch in 'mno':
        return 6
    elif ch in 'pqrs':
        return 7
    elif ch in 'tuv':
        return 8
    elif ch in 'wxyz':
        return 9
    
    return 0

def phoneWord2Num(word: str) -> int:
    word = word.lower()
    return helper_function(word[0])*pow(10, 6) + helper_function(word[1])*pow(10, 5) + helper_function(word[2])*pow(10, 4) + helper_function(word[3])*pow(10, 3) + helper_function(word[4])*pow(10, 2) + helper_function(word[5])*pow(10, 1) + helper_function(word[6])*pow(10, 0)
