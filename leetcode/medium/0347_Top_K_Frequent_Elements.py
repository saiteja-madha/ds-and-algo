# https://leetcode.com/problems/top-k-frequent-elements/
# tags: hashing

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}
        freq = [[] for _ in range(len(nums) + 1)]

        # store occurrence count
        for num in nums:
            my_map[num] = 1 + my_map.get(num, 0)

        # key is count, value is array of matching num
        for num, c in my_map.items():
            freq[c].append(num)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                break

        return res


print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
print(Solution().topKFrequent([1], 1))  # [1]
