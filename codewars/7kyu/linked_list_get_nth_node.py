#!/usr/bin/env python3

"""
Solution to http://www.codewars.com/kata/linked-lists-get-nth-node/

Linked Lists - Get Nth

Implement a GetNth() function that takes a linked list and an integer index and
returns the node stored at the Nth index position. GetNth() uses the C
numbering convention that the first node is index 0, the second is index 1,
... and so on. So for the list 42 -> 13 -> 666, GetNth() with index 1 should
return Node(13);

getNth(1 -> 2 -> 3 -> null, 0).data === 1
getNth(1 -> 2 -> 3 -> null, 1).data === 2

The index should be in the range [0..length-1]. If it is not, GetNth() should
throw/raise an exception (ArgumentException in C#, InvalidArgumentException in
PHP). You should also raise an exception (ArgumentException in C#,
InvalidArgumentException in PHP) if the list is empty/null/None.
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def get_nth(node, index):
    if node is None:
        raise IndexError("Index out of range")
    if index == 0:
        return node
    return get_nth(node.next, index - 1)
