# https://leetcode.com/problems/sliding-window-maximum/

import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        res = []
        for i, num in enumerate(nums):
            # Remove indices that are out of the current window
            if queue and queue[0] < i - k + 1:
                queue.popleft()

            # remove smaller values from right
            while queue and nums[queue[-1]] < num:
                queue.pop()

            queue.append(i)

            # After `k` elements, append the max of current window to the result
            if i >= k - 1:
                res.append(nums[queue[0]])

        return res


# Example 1
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
assert Solution().maxSlidingWindow(nums, k) == [3, 3, 5, 5, 6, 7]

# Example 2
nums = [1]
k = 1
assert Solution().maxSlidingWindow(nums, k) == [1]
