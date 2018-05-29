#!#!/usr/bin/env python2

"""
The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that character appears only once in the original string, or ')' if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples:

"din" => "((("

"recede" => "()()()"

"Success" => ")())())"

"(( @" => "))(("
"""

from collections import defaultdict


def count_letters(word):
    counts = defaultdict(int)
    for letter in word:
        counts[letter] += 1
    return counts


def duplicate_encode(word):
    lower = word.lower()
    counts = count_letters(lower)
    return ''.join(
        "(" if counts[letter] == 1 else ")"
        for letter in lower
    )
