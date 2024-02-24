# https://leetcode.com/problems/middle-of-the-linked-list/

from typing import Optional
from __utils import ListNode, list_to_linked_list, linked_list_to_list


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# Example 1:
head = list_to_linked_list([1, 2, 3, 4, 5])
expected = [3, 4, 5]
assert linked_list_to_list(Solution().middleNode(head)) == expected

# Example 2:
head = list_to_linked_list([1, 2, 3, 4, 5, 6])
expected = [4, 5, 6]
assert linked_list_to_list(Solution().middleNode(head)) == expected
