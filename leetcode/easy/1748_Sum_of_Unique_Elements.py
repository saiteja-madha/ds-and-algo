# https://leetcode.com/problems/sum-of-unique-elements/
# tags: hashing

# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
# Return the sum of all the unique elements of nums.

# Example 1:
# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.

# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: 0
# Explanation: There are no unique elements, and the sum is 0.

# Example 3:
# Input: nums = [1,2,3,4,5]
# Output: 15
# Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.

# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100

from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        my_map = {}
        for num in nums:
            my_map[num] = 1 + my_map.get(num, 0)
        res = 0
        print(my_map)
        for num, count in my_map.items():
            if count == 1:
                res += num
        return res


print(Solution().sumOfUnique([1,2,3,2])) # 4
print(Solution().sumOfUnique([1,1,1,1,1])) # 0
print(Solution().sumOfUnique([1,2,3,4,5])) # 15
