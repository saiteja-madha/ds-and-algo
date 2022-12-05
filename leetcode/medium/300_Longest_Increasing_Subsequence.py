# https://leetcode.com/problems/longest-increasing-subsequence/
# tags: dynamic programming
#
# Given an integer array nums, return the length of the longest strictly increasing
# subsequence.

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)


print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

print(Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]))  # 4

print(Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))  # 1
