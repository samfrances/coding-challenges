#!/usr/bin/env python3

"""
Solution to https://www.codewars.com/kata/5842df8ccbd22792a4000245/

You will be given a number and you will need to return it as a string in
Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'

NOTE: All numbers will be whole numbers greater than 0.
"""


def expanded_form(num):

    place_values = times10()
    face_values = mods(num, 10)
    face_with_place = zip(place_values, face_values)

    expanded = filter(lambda x: x > 0, (f * p for (f, p) in face_with_place))
    return ' + '.join(reversed([str(i) for i in expanded]))


def mods(num, divide_by):
    while num != 0:
        num, rem = num // divide_by, num % divide_by
        yield rem


def times10():
    n = 1
    while True:
        yield n
        n *= 10
