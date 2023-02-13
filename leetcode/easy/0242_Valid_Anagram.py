# https://leetcode.com/problems/valid-anagram/
# tags: hashing

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for ch in s:
            if ch in map:
                map[ch] = map[ch] + 1
            else:
                map[ch] = 1
        for ch in t:
            if ch in map:
                map[ch] = map[ch] - 1
            else:
                return False
        for k in map:
            if map[k] != 0:
                return False
        return True


print(Solution().isAnagram("anagram", "nagaram"))  # true
print(Solution().isAnagram("rat", "car"))  # false
