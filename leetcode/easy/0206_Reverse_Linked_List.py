# https://leetcode.com/problems/reverse-linked-list/
# tags: linked-list

# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
# Example 2:
# Input: head = [1,2]
# Output: [2,1]
#
# Example 3:
# Input: head = []
# Output: []

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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


list = ListNode(1).add(2).add(3).add(4).add(5)
print(Solution().reverseList(list))

list = ListNode(1).add(2)
print(Solution().reverseList(list))

list = None
print(Solution().reverseList(list))
