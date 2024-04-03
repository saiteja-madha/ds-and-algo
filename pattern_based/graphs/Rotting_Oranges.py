# https://leetcode.com/problems/rotting-oranges/

from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 0
        while q and fresh:
            minutes += 1
            size = len(q)

            for _ in range(size):
                r, c = q.popleft()

                for x, y in directions:
                    row, col = r + x, c + y
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                        fresh -= 1
                        grid[row][col] = 2
                        q.append((row, col))

        return minutes if fresh == 0 else -1


# Example 1:
grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
assert Solution().orangesRotting(grid) == 4

# Example 2:
grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
assert Solution().orangesRotting(grid) == -1

# Example 3:
grid = [[0, 2]]
assert Solution().orangesRotting(grid) == 0
