# https://leetcode.com/problems/longest-consecutive-sequence/
# tags: arrays, hashing

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1
        
        data = set(nums)
        cur_max = 1

        for num in data:
            prev = num - 1
            if prev not in data:
                c = 1
                nxt = num + 1
                while nxt in data:
                    nxt = nxt + 1
                    c += 1
                cur_max = max(cur_max, c)

        return cur_max


print(Solution().longestConsecutive([100,4,200,1,3,2])) # 4
print(Solution().longestConsecutive([])) # 0
print(Solution().longestConsecutive([0, 0])) # 1
print(Solution().longestConsecutive([0])) # 1
print(Solution().longestConsecutive([0,-1])) # 2