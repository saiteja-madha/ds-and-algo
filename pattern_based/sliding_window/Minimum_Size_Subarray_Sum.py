# https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        l, total = 0, 0

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        return res if res != float("inf") else 0


# Example 1
target = 7
nums = [2, 3, 1, 2, 4, 3]
assert Solution().minSubArrayLen(target, nums) == 2

# Example 2
target = 4
nums = [1, 4, 4]
assert Solution().minSubArrayLen(target, nums) == 1

# Example 3
target = 11
nums = [1, 1, 1, 1, 1, 1, 1, 1]
assert Solution().minSubArrayLen(target, nums) == 0
