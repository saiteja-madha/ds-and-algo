# https://leetcode.com/problems/middle-of-the-linked-list/
# tags: linked-list

# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
#
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
#
# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
#
# Constraints:
# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100

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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


list = ListNode(1).add(2).add(3).add(4).add(5)
print(Solution().middleNode(list))  # 3

list = ListNode(1).add(2).add(3).add(4).add(5).add(6)
print(Solution().middleNode(list))  # 4
