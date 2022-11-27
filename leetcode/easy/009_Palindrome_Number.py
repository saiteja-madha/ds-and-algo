# https://leetcode.com/problems/palindrome-number/
#
# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev = 0
        while x > 0:
            rev = rev * 10 + (x % 10)
            x = x // 10
        return temp == rev


print(Solution().isPalindrome(121))  # True
