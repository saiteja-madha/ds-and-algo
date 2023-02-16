# https://leetcode.com/problems/merge-two-sorted-lists/
# tags: linked-list

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

from typing import Optional


class ListNode:
    # Definition for singly-linked list.
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr_1 = ListNode()
        curr_1.next = list1
        curr_2 = list2
        while curr_2:
            itr = curr_1
            while itr.next and itr.next.val < curr_2.val:
                itr = itr.next

            temp = itr.next
            temp2 = curr_2.next

            curr_2.next = temp
            itr.next = curr_2

            curr_2 = temp2
        return curr_1.next


list1 = ListNode(1).add(2).add(4)
list2 = ListNode(1).add(3).add(4)
print(Solution().mergeTwoLists(list1, list2))  # [1,1,2,3,4,4]
