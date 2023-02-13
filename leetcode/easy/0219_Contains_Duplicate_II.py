# https://leetcode.com/problems/contains-duplicate-ii/
# tags: hashing

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

# Constraints:
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 0 <= k <= 10^5

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, num in enumerate(nums):
            if not num in dic:
                dic[num] = i
            else:
                if abs(i - dic[num]) <= k:
                    return True
                else:
                    dic[num] = i
        return False


print(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))  # true
print(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))  # true
print(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))  # false
