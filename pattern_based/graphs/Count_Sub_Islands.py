# https://leetcode.com/problems/count-sub-islands/

from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        visited = set()

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid2[r][c] == 0 or (r, c) in visited:
                return True

            visited.add((r, c))
            res = True
            if grid1[r][c] == 0:
                res = False

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x, y in directions:
                res = dfs(r + x, c + y) and res

            return res

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] and (r, c) not in visited and dfs(r, c):
                    count += 1
        return count


# Example 1:
grid1 = [
    [1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1],
]
grid2 = [
    [1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1],
]

assert (result := Solution().countSubIslands(grid1, grid2)) == 3, result

# Example 2:
grid1 = [
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
]
grid2 = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]]

assert (result := Solution().countSubIslands(grid1, grid2)) == 2, result
