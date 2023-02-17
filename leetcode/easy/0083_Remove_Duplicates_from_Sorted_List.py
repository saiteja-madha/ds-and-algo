# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# tags: linked-list

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]

# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

# Constraints:
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        my_set = set()
        dummy = ListNode(0, head)
        prev, ptr = dummy, head
        while ptr:
            if ptr.val in my_set:
                prev.next = ptr.next
            else:
                my_set.add(ptr.val)
                prev = prev.next
            ptr = ptr.next
        return dummy.next


list = ListNode(1).add(1).add(2)
print(Solution().deleteDuplicates(list))  # [1, 2]

list = ListNode(1).add(1).add(2).add(3).add(3)
print(Solution().deleteDuplicates(list))  # [1, 2, 3]
