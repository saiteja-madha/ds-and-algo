# Fibonacci of a Number
# https://leetcode.com/problems/fibonacci-number/

# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.
# That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).


# Using recursion
def fib_rec(num):
    if num == 0:
        return 0
    if num <= 2:
        return 1
    return fib_rec(num - 1) + fib_rec(num - 2)


# Using dp and memoization
def fib_dp(num, memo={}):
    if num in memo:
        return memo[num]
    if num == 0:
        return 0
    if num <= 2:
        return 1
    memo[num] = fib_dp(num - 1, memo) + fib_dp(num - 2, memo)
    return memo[num]


print(fib_rec(30))  # 832040
print(fib_dp(100))  # 354224848179261915075
