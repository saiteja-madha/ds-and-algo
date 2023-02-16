# https://leetcode.com/problems/remove-linked-list-elements/
# tags: linked-list

# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Example 2:
# Input: head = [], val = 1
# Output: []

# Example 3:
# Input: head = [7,7,7,7], val = 7
# Output: []

# Constraints:
# The number of nodes in the list is in the range [0, 104].
# 1 <= Node.val <= 50
# 0 <= val <= 50

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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # prev, ptr = None, head
        # while ptr:
        #     if ptr.val == val:
        #         if not prev:
        #             prev = ptr
        #         else:
        #             prev.next = ptr.next
        #     else:
        #         prev = prev.next if prev else head
        #     ptr = ptr.next
        # return head if head and head.val != val else head.next

        # Neetcode
        dummy = ListNode(0, head)
        prev, ptr = dummy, head
        while ptr:
            if ptr.val == val:
                prev.next = ptr.next
            else:
                prev = prev.next
            ptr = ptr.next
        return dummy.next


list = ListNode(1).add(2).add(6).add(3).add(4).add(5).add(6)
print(Solution().removeElements(list, 6))  # [1,2,3,4,5]

list = ListNode(0)
print(Solution().removeElements(list, 1))  # []

list = ListNode(7).add(7).add(7).add(7)
print(Solution().removeElements(list, 7))  # []

list = ListNode(1).add(2)
print(Solution().removeElements(list, 1))  # [2]
