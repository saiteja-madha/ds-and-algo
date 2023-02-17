# https://leetcode.com/problems/intersection-of-two-linked-lists/
# tags: linked-list

# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
# If the two linked lists have no intersection at all, return null.

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def add(self, val):
        if self.next is None:
            self.next = ListNode(val)
        else:
            self.next.add(val)
        return self

    def __str__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        my_set = set()
        ptr = headA
        while ptr:
            my_set.add(id(ptr))
            ptr = ptr.next
        ptr = headB
        while ptr:
            if id(ptr) in my_set:
                return ptr
            ptr = ptr.next
        return None
