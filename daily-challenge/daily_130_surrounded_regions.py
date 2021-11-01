"""
- Modify the input in place
- iterate each row and cell
- if the current cell is O,
  - if four directions are X, update it to X
- return modified input

- Time is O(nm)
- Space is O(1)
"""


from typing import List
import itertools


class Solution:
    def __init__(self):
        self.ROWS = 0
        self.COLS = 0

    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        self.ROWS = len(board)
        self.COLS = len(board[0])

        borders = (
            # cells at left and right column in all the rows
            list(itertools.product(range(self.ROWS), [0, self.COLS - 1]))
            # cells at top and bottom in all the column
            + list(itertools.product([0, self.ROWS - 1], range(self.COLS)))
        )

        # Mark the O cells at the border and O cells connected to O cells at the border to E
        for row, col in borders:
            self.DFS(board, row, col)

        for row in range(self.ROWS):
            for col in range(self.COLS):
                # After the above DFS, the remaining O are the cells not connected to border Os,
                # so they are surrounded by X in the board
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'E':
                    board[row][col] = 'O'

        # [print(row) for row in board]

    def DFS(self, board, row, col):
        # If the current cell is either X or E, no need to check
        if board[row][col] != 'O':
            return

        board[row][col] = 'E'

        # Recursively find another cell which are O at the border
        if col < self.COLS - 1:
            self.DFS(board, row, col + 1)

        if row < self.ROWS - 1:
            self.DFS(board, row + 1, col)

        if col > 0:
            self.DFS(board, row, col - 1)

        if row > 0:
            self.DFS(board, row - 1, col)


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(Solution().solve(board))
