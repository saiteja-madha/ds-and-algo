# https://leetcode.com/problems/length-of-last-word/

# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

import re


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(re.split(r'\s+', s.strip())[-1])


print(Solution().lengthOfLastWord("Hello World"))  # 5
print(Solution().lengthOfLastWord("   fly me   to   the moon  "))  # 4
print(Solution().lengthOfLastWord("luffy is still joyboy"))  # 6
print(Solution().lengthOfLastWord(""))  # 0
