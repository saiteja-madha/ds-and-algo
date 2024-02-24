# https://leetcode.com/problems/3sum/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums) - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])

                if s <= 0:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                if s > 0:
                    r -= 1

        return res


# Example 1:
nums = [-1, 0, 1, 2, -1, -4]
assert Solution().threeSum(nums) == [[-1, -1, 2], [-1, 0, 1]]

# Example 2:
nums = [0, 1, 1]
assert Solution().threeSum(nums) == []

# Example 3:
nums = [0, 0, 0]
assert Solution().threeSum(nums) == [[0, 0, 0]]
