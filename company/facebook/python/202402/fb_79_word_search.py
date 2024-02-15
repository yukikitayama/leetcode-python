"""
DFS(r, c, i)
  r c identifies the location in board
  i identifies current character to find from word ith character
  visited set collect (row, col) to avoid visiting again
    recursion as long as next row col are in the board and next character matches
  Terminate recursion if i equal to length of word

for each cell as start of DFS if it matches with word first character

eg
[
    ["A","B","C","E"],
    ["S","F","E","S"],
    ["A","D","E","E"]
    ]
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtracking(r, c, i):

            if i == len(word):
                return True

            if r < 0 or len(board) == r or c < 0 or len(board[0]) == c or board[r][c] != word[i]:
                return False

            ans = False
            board[r][c] = "#"
            for offset_r, offset_c in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                next_r = r + offset_r
                next_c = c + offset_c
                ans = backtracking(next_r, next_c, i + 1)
                if ans:
                    break

            # Backtrack
            board[r][c] = word[i]

            return ans

        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtracking(r, c, 0):
                    return True

        return False
