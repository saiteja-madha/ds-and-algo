# https://leetcode.com/problems/plus-one/
#
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        toAdd = 1
        for i in range(len(digits) - 1, -1, -1):
            if toAdd == 1:
                if digits[i] == 9:
                    digits[i] = 0
                    toAdd = 1
                    if i == 0:
                        digits.insert(0, 1)
                else:
                    digits[i] += 1
                    toAdd = 0
            else:
                break  # No need to check remaining
        return digits


print(Solution().plusOne([1, 2, 3]))  # [1, 2, 4]
print(Solution().plusOne([4, 3, 2, 1]))  # [4, 3, 2, 2]
print(Solution().plusOne([9]))  # [1, 0]
