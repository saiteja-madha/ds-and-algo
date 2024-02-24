# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional
from __utils import ListNode, list_to_linked_list, linked_list_to_list


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None

        r = head
        for _ in range(n):
            r = r.next

        l = head
        if r == None:
            return head.next

        while r != None and r.next != None:
            r = r.next
            l = l.next
        l.next = l.next.next
        return head


# Example 1
head = list_to_linked_list([1, 2, 3, 4, 5])
n = 2
expected = [1, 2, 3, 5]
assert linked_list_to_list(Solution().removeNthFromEnd(head, n)) == expected

# Example 2
head = list_to_linked_list([1])
n = 1
expected = []
assert linked_list_to_list(Solution().removeNthFromEnd(head, n)) == expected

# Example 3
head = list_to_linked_list([1, 2])
n = 1
expected = [1]
assert linked_list_to_list(Solution().removeNthFromEnd(head, n)) == expected
