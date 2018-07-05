#!/usr/bin/env python3

"""
Solution to http://www.codewars.com/kata/55beec7dd347078289000021/

Linked Lists - Length & Count

Implement Length() to count the number of nodes in a linked list.

length(null) => 0
length(1 -> 2 -> 3 -> null) => 3
Implement Count() to count the occurrences of an integer in a linked list.

count(null, 1) => 0
count(1 -> 2 -> 3 -> null, 1) => 1
count(1 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 3 -> 3 -> null, 2) => 4
"""

from collections import Counter


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def iter_ll(node):
    while True:
        yield node.data
        if node.next is None:
            return
        node = node.next


def length(node):
    if node is None:
        return 0
    return len(list(iter_ll(node)))


def count(node, data):
    if node is None:
        return 0
    return Counter(iter_ll(node))[data]
