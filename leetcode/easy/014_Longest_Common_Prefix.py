# https://leetcode.com/problems/longest-common-prefix/

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort(key=len)
        first = strs[0]
        remaining = strs[1:]

        def compare(input: str):
            for str in remaining:
                if not str.startswith(input):
                    return False
            return True

        output = ""
        for i in range(len(first), -1, -1):
            check = first[0:i]
            exists = compare(check)
            if exists:
                output = check
                break
        return output


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))  # "fl"
print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))  # ""
print(Solution().longestCommonPrefix(["reflower", "flow", "flight"]))  # ""
