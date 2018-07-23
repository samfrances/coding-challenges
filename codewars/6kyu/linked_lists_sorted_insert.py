#!/usr/bin/env python3

"""
Solution to http://www.codewars.com/kata/linked-lists-sorted-insert/

Linked Lists - Sorted Insert

Write a SortedInsert() function which inserts a node into the correct location
of a pre-sorted linked list which is sorted in ascending order. SortedInsert
takes the head of a linked list and data used to create a node as arguments.
SortedInsert() should also return the head of the list.

sortedInsert(1 -> 2 -> 3 -> null, 4) === 1 -> 2 -> 3 -> 4 -> null)
sortedInsert(1 -> 7 -> 8 -> null, 5) === 1 -> 5 -> 7 -> 8 -> null)
sortedInsert(3 -> 5 -> 9 -> null, 7) === 3 -> 5 -> 7 -> 9 -> null)

The push() and buildOneTwoThree() functions do not need to be redefined.
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_insert(head, data):
    if head is None or head.data > data:
        new_head = Node(data)
        new_head.next = head
        return new_head
    head.next = sorted_insert(head.next, data)
    return head
