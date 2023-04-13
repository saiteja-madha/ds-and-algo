# https://leetcode.com/problems/valid-sudoku/
# tags: arrays, hashing

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


# Example 1:
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:
#
# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.


from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            data = set()
            for j in range(9):
                el = board[i][j]
                if el != ".":
                    if el in data:
                        return False
                    data.add(el)

        for i in range(9):
            data = set()
            for j in range(9):
                el = board[j][i]
                if el != ".":
                    if el in data:
                        return False
                    data.add(el)

        dia = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3),
               (3, 6), (6, 0), (6, 3), (6, 6)]
        for x, y in dia:
            data = set()
            for i in range(0, 3):
                for j in range(0, 3):
                    el = board[x+i][y+j]
                    if el != ".":
                        if el in data:
                            return False
                        data.add(el)

        return True


print(Solution().isValidSudoku([[".", ".", ".", ".", "5", ".", ".", "1", "."],
                                [".", "4", ".", "3", ".", ".", ".", ".", "."],
                                [".", ".", ".", ".", ".", "3", ".", ".", "1"],
                                ["8", ".", ".", ".", ".", ".", ".", "2", "."],
                                [".", ".", "2", ".", "7", ".", ".", ".", "."],
                                [".", "1", "5", ".", ".", ".", ".", ".", "."],
                                [".", ".", ".", ".", ".", "2", ".", ".", "."],
                                [".", "2", ".", "9", ".", ".", ".", ".", "."],
                                [".", ".", "4", ".", ".", ".", ".", ".", "."]
                                ]))
