# https://leetcode.com/problems/contains-duplicate/
# tags: hashing

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Constraints:
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


print(Solution().containsDuplicate([1,2,3,1])) # True
print(Solution().containsDuplicate([1,2,3,4])) # False
print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # True
