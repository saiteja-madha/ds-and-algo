# https://leetcode.com/problems/minimum-window-substring/


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resL = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # if we have a character we need is exact match
            if c in countT and window[c] == countT[c]:
                have += 1

            # if we have all the characters we need
            while have == need:
                # update our result
                if (r - l + 1) < resL:
                    res = [l, r]
                    resL = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resL != float("inf") else ""


# Example 1:
s = "ADOBECODEBANC"
t = "ABC"
assert Solution().minWindow(s, t) == "BANC"

# Example 2:
s = "a"
t = "a"
assert Solution().minWindow(s, t) == "a"

# Example 3:
s = "a"
t = "aa"
assert Solution().minWindow(s, t) == ""
