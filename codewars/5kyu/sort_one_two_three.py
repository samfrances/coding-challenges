#!/usr/bin/env python3.6

"""
Solution to: http://www.codewars.com/kata/56f4ff45af5b1f8cd100067d/


Hey You !

Sort these integers for me ...

By name ...

Do it now !
Input

    Range is 0-999

    There may be duplicates

    The array may be empty

"""


def sort_by_name(arr):
    return sorted(arr, key=name_number)


digits = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten"
}

teens = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

tens = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

precalculated = dict(
    ({0: "zero"}).items() |
    digits.items() |
    teens.items() |
    tens.items()
)


def decompose(num):
    """
    Decompose a number between 0 and 999 into a hundreds component, a tens
    component and a units component, such that
    hundreds + tens + units == original number
    """
    hundreds = (num // 100) * 100
    rem = num % 100
    tens = (rem // 10) * 10
    units = rem % 10

    return hundreds, tens, units


def name_number(num):
    if num in precalculated:
        return precalculated[num]

    hundreds, tens, units = decompose(num)

    if num < 100:
        return name_number(tens) + name_number(units)
    elif not (tens or units):
        return "{} hundred".format(name_number(hundreds // 100))
    else:
        return "{} and {}".format(
            name_number(hundreds),
            name_number(tens + units),
        )
