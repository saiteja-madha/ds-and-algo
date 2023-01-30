# https://leetcode.com/problems/climbing-stairs/
# tags: dynamic programming

# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:
# 1 <= n <= 45

class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0] * n
        for i in range(n - 1, -1, -1):
            if i == n-1: arr[i] = 1
            elif i == n-2: arr[i] = 2
            else:
                arr[i] = arr[i+1] + arr[i+2]
        return arr[0]
    
print(Solution().climbStairs(2))  # 2
print(Solution().climbStairs(3))  # 3