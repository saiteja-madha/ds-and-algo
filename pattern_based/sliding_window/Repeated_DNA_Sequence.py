# https://leetcode.com/problems/repeated-dna-sequences/

from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        data = {}
        for i in range(0, len(s) - 9):
            sub = s[i : i + 10]
            data[sub] = data.get(sub, 0) + 1

        res = []
        for k, v in data.items():
            if v > 1:
                res.append(k)
        return res


# Example 1
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
assert Solution().findRepeatedDnaSequences(s) == ["AAAAACCCCC", "CCCCCAAAAA"]

# Example 2
s = "AAAAAAAAAAAAA"
assert Solution().findRepeatedDnaSequences(s) == ["AAAAAAAAAA"]
