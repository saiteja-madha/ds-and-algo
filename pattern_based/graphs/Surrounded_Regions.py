# https://leetcode.com/problems/surrounded-regions/

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        visit = set()

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or board[r][c] == "X" or (r, c) in visit:
                return

            visit.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x, y in directions:
                dfs(r + x, c + y)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visit:
                    board[r][c] = "X"


# Example 1:
board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
output = [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
Solution().solve(board)
assert board == output

# Example 2:
board = [["X"]]
output = [["X"]]
Solution().solve(board)
assert board == output
