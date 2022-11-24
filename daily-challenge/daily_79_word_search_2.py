"""
- Backtracking, try all the cells as a start cell
- Or dp
- Trie
"""


from typing import List


class Solution:
    def __init__(self):
        self.board = None

    def exist(self, board: List[List[str]], word: str) -> bool:

        self.board = board

        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.backtracking(r, c, word):
                    return True

        return False

    def backtracking(self, r, c, suffix) -> bool:
        if len(suffix) == 0:
            return True

        if r < 0 or r == len(self.board) or c < 0 or c == len(self.board[0]) or self.board[r][c] != suffix[0]:
            return False

        self.board[r][c] = '#'

        for r_offset, c_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

            if self.backtracking(r + r_offset, c + c_offset, suffix[1:]):
                return True

        self.board[r][c] = suffix[0]

        return False
