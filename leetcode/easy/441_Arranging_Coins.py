# https://leetcode.com/problems/arranging-coins/

# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.

# Example 1:
# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.

# Example 2:
# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.
 
# Constraints:
# 1 <= n <= 2^31 - 1

class Solution:
    def arrangeCoins(self, n: int) -> int:
        used, rem = 0, n
        last = 0
        for i in range(1, n + 1):
            if rem < i:
                return i -1
            used += i
            rem = n - used
            last = i
        return last
    
print(Solution().arrangeCoins(5))  # 2
print(Solution().arrangeCoins(8))  # 3