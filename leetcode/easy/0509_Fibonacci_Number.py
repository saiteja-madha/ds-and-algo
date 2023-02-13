# https://leetcode.com/problems/fibonacci-number/

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.
# That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).


class Solution:
    # Using dp and memoization
    def fib(self, n: int, mem={}) -> int:
        if n in mem:
            return mem[n]
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        temp = self.fib(n-1, mem) + self.fib(n-2, mem)
        mem[n] = temp
        return temp

    # Using recursion
    def fib_rec(self, num):
        if num == 0:
            return 0
        if num <= 2:
            return 1
        return self.fib_rec(num - 1) + self.fib_rec(num - 2)


print(Solution().fib_rec(30))  # 832040
print(Solution().fib(100))  # 354224848179261915075
