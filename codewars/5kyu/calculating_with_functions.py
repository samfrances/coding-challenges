"""
Solution to https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/

This time we want to write calculations using functions and get the results.
Let's have a look at some examples:

JavaScript:

seven(times(five())); // must return 35
four(plus(nine())); // must return 13
eight(minus(three())); // must return 5
six(dividedBy(two())); // must return 3

Ruby:

seven(times(five)) # must return 35
four(plus(nine)) # must return 13
eight(minus(three)) # must return 5
six(divided_by(two)) # must return 3

Requirements:

    There must be a function for each number from 0 ("zero") to 9 ("nine")
    There must be a function for each of the following mathematical
        operations: plus, minus, times, dividedBy (divided_by in Ruby)
    Each calculation consist of exactly one operation and two numbers
    The most outer function represents the left operand, the most inner
        function represents the right operand
    Divison should be integer division,
        e.g eight(dividedBy(three()))/eight(divided_by(three))
        should return 2, not 2.666666...

"""

from operator import add, mul, floordiv, sub


def _number(n):
    def numfunc(operator=None):
        if operator:
            return operator(n)
        return n
    return numfunc


def _operator(f):
    def op(n):
        def op_n(i):
            return f(i, n)
        return op_n
    return op


zero = _number(0)
one = _number(1)
two = _number(2)
three = _number(3)
four = _number(4)
five = _number(5)
six = _number(6)
seven = _number(7)
eight = _number(8)
nine = _number(9)

plus = _operator(add)
minus = _operator(sub)
times = _operator(mul)
divided_by = _operator(floordiv)
