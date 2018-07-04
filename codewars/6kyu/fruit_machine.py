#!/usr/env/bin python3

"""
Solution to https://www.codewars.com/kata/590adadea658017d90000039/
"""


from itertools import count
from collections import Counter

FACES = ["Jack", "Queen", "King", "Bar", "Cherry", "Seven", "Shell", "Bell", "Star", "Wild"]
BASE_SCORES = dict(zip(FACES, count(1)))


def fruit(reels, spins):
    faces = Counter(reels[i][spins[i]] for i in range(3))
    counts_to_faces = {count: face for (face, count) in faces.items()}
    if len(faces) == 1:
        face = counts_to_faces[3]
        return three_of_the_same(face)
    if len(faces) == 2:
        face = counts_to_faces[2]
        return two_of_the_same(
            face,
            faces["Wild"] == 1
        )
    return 0


def three_of_the_same(face):
    return BASE_SCORES[face] * 10


def two_of_the_same(face, plus_wild=False):
    score = BASE_SCORES[face]
    return score * 2 if plus_wild else score
