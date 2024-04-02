# https://leetcode.com/problems/max-area-of-island/

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0 or (r, c) in visited:
                return 0

            visited.add((r, c))
            area = 1
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x, y in directions:
                area += dfs(r + x, c + y)
            return area

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    res = max(res, dfs(r, c))
        return res


# Example 1:
grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]
assert (result := Solution().maxAreaOfIsland(grid)) == 6, result

# Example 2:
grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
assert (result := Solution().maxAreaOfIsland(grid)) == 0, result
