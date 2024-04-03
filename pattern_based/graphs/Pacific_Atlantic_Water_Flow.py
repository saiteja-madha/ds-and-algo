# https://leetcode.com/problems/pacific-atlantic-water-flow/

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prev):
            if r not in range(ROWS) or c not in range(COLS) or heights[r][c] < prev or (r, c) in visit:
                return

            visit.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x, y in directions:
                dfs(r + x, c + y, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res


# Example 1:
heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
output = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
assert Solution().pacificAtlantic(heights) == output

# Example 2:
heights = [[2, 1], [1, 2]]
output = [[0, 0], [0, 1], [1, 0], [1, 1]]
assert Solution().pacificAtlantic(heights) == output
