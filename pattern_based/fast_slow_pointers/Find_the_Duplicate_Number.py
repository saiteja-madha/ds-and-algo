# https://leetcode.com/problems/find-the-duplicate-number/

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast


# Example 1:
nums = [1, 3, 4, 2, 2]
assert Solution().findDuplicate(nums) == 2

# Example 2:
nums = [3, 1, 3, 4, 2]
assert Solution().findDuplicate(nums) == 3
