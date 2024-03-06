# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        data = set()
        l, res = 0, 0
        for r in range(len(s)):
            while s[r] in data:
                data.remove(s[l])
                l += 1
            data.add(s[r])
            res = max(r - l + 1, res)
        return res


# Example 1
s = "abcabcbb"
assert Solution().lengthOfLongestSubstring(s) == 3

# Example 2
s = "bbbbb"
assert Solution().lengthOfLongestSubstring(s) == 1

# Example 3
s = "pwwkew"
assert Solution().lengthOfLongestSubstring(s) == 3
