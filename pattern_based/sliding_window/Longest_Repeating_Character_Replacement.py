# https://leetcode.com/problems/longest-repeating-character-replacement/


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        res = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res


# Example 1
s = "ABAB"
k = 2
assert Solution().characterReplacement(s, k) == 4

# Example 2
s = "AABABBA"
k = 1
assert Solution().characterReplacement(s, k) == 4
