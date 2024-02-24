# https://leetcode.com/problems/valid-palindrome-ii/


class Solution:
    @staticmethod
    def isPalindrome(s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return Solution.isPalindrome(s[l + 1 : r + 1]) or Solution.isPalindrome(s[l:r])
            l += 1
            r -= 1
        return True


# Example 1:
s = "aba"
assert Solution().validPalindrome(s) is True

# Example 2:
s = "abca"
assert Solution().validPalindrome(s) is True

# Example 3:
s = "abc"
assert Solution().validPalindrome(s) is False
