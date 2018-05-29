#!/usr/bin/env python2

"""
https://www.codewars.com/kata/576757b1df89ecf5bd00073b/

For example, a tower of 3 floors looks like below

[
  '  *  ',
  ' *** ',
  '*****'
]

and a tower of 6 floors looks like below

[
  '     *     ',
  '    ***    ',
  '   *****   ',
  '  *******  ',
  ' ********* ',
  '***********'
]

"""


def tower_builder(n_floors):
    base_len = 1 + (2 * (n_floors - 1))
    floors = []

    for i in range(n_floors):
        spaces = i * 2
        floor_len = base_len - spaces
        floors.append(
            (' ' * (spaces / 2)) +
            ('*' * floor_len) +
            (' ' * (spaces / 2))
        )

    return floors[::-1]
