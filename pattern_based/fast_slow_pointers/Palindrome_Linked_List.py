# https://leetcode.com/problems/palindrome-linked-list/

from typing import Optional
from __utils import ListNode, list_to_linked_list


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Finding Midpoint
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reversing the second half
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Checking if it's palindrome?
        first_half, reversed_half = head, prev
        while first_half and reversed_half:
            if first_half.val != reversed_half.val:
                return False

            first_half = first_half.next
            reversed_half = reversed_half.next

        return True


# Example 1
head = list_to_linked_list([1, 2, 2, 1])
expected = True
assert Solution().isPalindrome(head) == expected

# Example 2
head = list_to_linked_list([1, 2])
expected = False
assert Solution().isPalindrome(head) == expected
