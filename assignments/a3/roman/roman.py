# Assignment 3, Task 8
# Name: Jiraroj Wiruchpongsanon
# Collaborators: <NAME_1, NAME_2>
# Time Spent: 0.1 hrs
# Use of AI: NO
# AI usage details: <DETAILS>

# not allowed to use loops and other ds, makes the solution a lot less elegant

### Your code start here ######
def helper_function(digit: int, decimal: str, five: str, higher_decimal: str) -> str:
    if digit == 9:
        return decimal + higher_decimal
    if digit == 4:
        return decimal + five

    roman = ''
    if digit >= 5:
        roman += five
        digit -= 5
    roman += decimal * digit
    return roman


def toRoman(n: int) -> str:
    roman_number = ''

    units = n % 10
    n //= 10
    roman_number = helper_function(units, 'I', 'V', 'X') + roman_number

    tens = n % 10
    n //= 10
    roman_number = helper_function(tens, 'X', 'L', 'C') + roman_number

    hundreds = n % 10
    n //= 10
    roman_number = helper_function(hundreds, 'C', 'D', 'M') + roman_number

    thousands = n % 10
    n //= 10
    roman_number = helper_function(thousands, 'M', 'V̅', 'X̅') + roman_number

    return roman_number
