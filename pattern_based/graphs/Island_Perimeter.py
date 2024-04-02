# https://leetcode.com/problems/island-perimeter/

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0:
                return 1
            if (r, c) in visited:
                return 0
            visited.add((r, c))

            res = 0
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x, y in directions:
                res += dfs(r + x, c + y)
            return res

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)


# Example 1:
grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
assert (result := Solution().islandPerimeter(grid)) == 16, result

# Example 2:
grid = [[1]]
assert (result := Solution().islandPerimeter(grid)) == 4, result

# Example 3:
grid = [[1, 0]]
assert (result := Solution().islandPerimeter(grid)) == 4, result
