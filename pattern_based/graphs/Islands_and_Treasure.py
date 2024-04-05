# https://neetcode.io/problems/islands-and-treasure

from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        steps = 0
        while q:
            steps += 1
            for _ in range(len(q)):
                r, c = q.popleft()

                for x, y in directions:
                    row, col = r + x, c + y
                    if row not in range(rows) or col not in range(cols) or grid[row][col] == -1:
                        continue

                    if grid[row][col] != 0 and grid[row][col] > steps:
                        grid[row][col] = steps
                        q.append((row, col))

        return grid


# Example 1
grid = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647],
]
output = [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
assert Solution().islandsAndTreasure(grid) == output

# Example 2
grid = [[0, -1], [2147483647, 2147483647]]
output = [[0, -1], [1, 2]]
assert Solution().islandsAndTreasure(grid) == output
