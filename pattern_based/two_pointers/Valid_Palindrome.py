# https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            elif not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


# Example 1:
s = "A man, a plan, a canal: Panama"
assert Solution().isPalindrome(s) is True

# Example 2:
s = "race a car"
assert Solution().isPalindrome(s) is False

# Example 3:
s = " "
assert Solution().isPalindrome(s) is True
