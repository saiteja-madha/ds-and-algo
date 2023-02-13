# https://leetcode.com/problems/majority-element/

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than [n / 2] times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# Constraints:
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9

# Follow-up: Could you solve the problem in linear time and in O(1) space?

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        times = len(nums) / 2
        count = 1
        res = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            if num == res:
                count += 1
            else:
                count = 1
            if count > times:
                return res
            res = num
        return res


print(Solution().majorityElement([3, 2, 3]))  # 3
print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2
print(Solution().majorityElement([3, 3, 4]))  # 3
print(Solution().majorityElement([-1, 1, 1, 1, 2, 1]))  # 1
