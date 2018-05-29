#!/usr/bin/env python2

"""
https://www.codewars.com/kata/56606694ec01347ce800001b

Implement a method that accepts 3 integer values a, b, c. The method should
return true if a triangle can be built with the sides of given length and
false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

"""


def is_triangle(a, b, c):
    """
    Uses the Triange Inequality Theorem to determine if a triangle can be
    formed given the lengths of the three sides.

    https://en.wikipedia.org/wiki/Triangle_inequality
    """
    return (a + b) > c and (a + c) > b and (b + c) > a
