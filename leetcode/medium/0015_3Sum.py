# https://leetcode.com/problems/3sum/
# tags: 2-pointer

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

# Constraints:
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5

from typing import List


class Solution:

    # Runtime: 5915 ms (Beats 10.64%)
    # Memory : 19.5 MB (Beats 9.7%)
    def threeSum_1(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                return [[nums[0], nums[1], nums[2]]]
            else:
                return []

        res = set()
        m = {nums[0]: 0}
        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums)):
                s = 0 - (nums[i] + nums[j])
                if s in m and m[s] != i and m[s] != j:
                    arr = [nums[i], nums[j], nums[m[s]]]
                    arr.sort()
                    res.add(tuple(arr))
                m[nums[j]] = j

        sol = []
        for v in res:
            sol.append(list(v))

        return sol

    # Runtime: 3439 ms (Beats 19.18%)
    # Memory : 19.8 MB (Beats 5.68%)
    def threeSum_2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(0, len(nums)):
            l, r = i+1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1

        sol = []
        for v in res:
            sol.append(list(v))

        return sol

    # Runtime: 1739 ms (Beats 39.47%)
    # Memory : 18.5 MB (Beats 38.6%)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums) - 2):
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

    # Runtime: 1395 ms (Beats 62.71%)
    # Memory : 18.4 MB (Beats 60.67%)
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


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
print(Solution().threeSum([0, 1, 1]))  # []
print(Solution().threeSum([0, 0, 0]))  # [[0,0,0]]
print(Solution().threeSum([0, 0, 0, 0]))  # [[0,0,0]]
print(Solution().threeSum([1, 2, -2, -1]))  # []
print(Solution().threeSum([3, -2, 1, 0]))  # []
print(Solution().threeSum([1, -1, -1, 0]))  # [[-1,0,1]]
print(Solution().threeSum([-2, 0, 1, 1, 2]))  # [[-2,0,2],[-2,1,1]]
print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
