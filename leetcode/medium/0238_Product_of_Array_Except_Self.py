# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Constraints:
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [nums[0]]
        for i in range(1, len(nums)):
            l = left[i - 1]
            left.append(l * nums[i])
        
        right = [0] * len(nums)
        right[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, 0, -1):
            r = right[i + 1]
            right[i] = r * nums[i]

        res = [0] * len(nums)
        res[0] = right[1]
        res[len(nums) - 1] = left[len(nums) - 2]
        for i in range(1, len(nums) - 1):
            res[i] = left[i - 1] * right[i + 1]
        return res