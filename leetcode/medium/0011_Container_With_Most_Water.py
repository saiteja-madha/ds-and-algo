# https://leetcode.com/problems/container-with-most-water/
# tags: 2-pointer

# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

# Constraints:
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4

from typing import List


class Solution:
    # Brute Force
    def maxArea_1(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                area = min(height[i], height[j]) * (j - i)
                res = max(res, area)
        return res

    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            res = max(area, res)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
print(Solution().maxArea([1, 1]))  # 1
print(Solution().maxArea([1, 2, 4, 3]))  # 4
