# https://leetcode.com/problems/reverse-words-in-a-string/


class Solution:

    def reverseWords(self, s: str) -> str:
        s = s[::-1]
        l, r = 0, 0
        res = ""
        while r < len(s):
            if s[l] != " ":
                while r < len(s) and s[r] != " ":
                    r += 1
                res += s[l:r][::-1] + " "
            r += 1
            l = r
        return res[: len(res) - 1]


# Example 1:
s = "the sky is blue"
assert Solution().reverseWords(s) == "blue is sky the"

# Example 2:
s = "  hello world  "
assert Solution().reverseWords(s) == "world hello"

# Example 3:
s = "a good   example"
assert Solution().reverseWords(s) == "example good a"
