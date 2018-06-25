#!/usr/bin/env python2

"""
Solution to https://www.codewars.com/kata/5838b5eb1adeb6b7220000f5/
"""


from collections import Counter, defaultdict
from itertools import chain


def id_best_users(*args):
    # your code here
    best_users = set.intersection(*map(set, args))
    tallies = Counter(user for user in chain.from_iterable(args) if user in best_users)
    inverted = inverted_tallies(tallies)
    inverted_items = [list(pair) for pair in inverted.items()]
    return list(reversed(sorted(list(inverted_items))))


def inverted_tallies(tallies):
    inverted = defaultdict(list)
    for user_id in sorted(tallies.keys()):
        inverted[tallies[user_id]].append(user_id)
    return inverted
