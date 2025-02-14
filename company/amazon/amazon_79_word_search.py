"""
dfs(r, c, i)
  return true if i is length of word
  recursion if the next from the grid is the next character
"""

from typing import List


class Solution:
    def exist3(self, board: List[List[str]], word: str) -> bool:

        def backtracking(row, col, index, visited):

            if index == len(word) - 1:
                return True

            res = False
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr = row + dr
                nc = col + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                    if board[nr][nc] == word[index + 1] and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        res |= backtracking(nr, nc, index + 1, visited)
                        visited.remove((nr, nc))

            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    visited = set()
                    visited.add((r, c))
                    if backtracking(r, c, 0, visited):
                        return True

        return False

    def exist2(self, board: List[List[str]], word: str) -> bool:

        def backtracking(row, col, index):

            if row < 0 or row == len(board) or col < 0 or col == len(board[0]) or board[row][col] != word[index]:
                return False

            if index == len(word) - 1:
                return True

            original = board[row][col]
            board[row][col] = "#"

            res = False
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr = row + dr
                nc = col + dc
                res |= backtracking(nr, nc, index + 1)

            board[row][col] = original

            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtracking(r, c, 0):
                    return True

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(row, col, index, visited):

            if index == len(word) - 1:
                return True

            res = False
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_r = row + dr
                next_c = col + dc
                if 0 <= next_r < len(board) and 0 <= next_c < len(board[0]):
                    if board[next_r][next_c] == word[index + 1] and (next_r, next_c) not in visited:
                        visited.add((next_r, next_c))
                        res |= dfs(next_r, next_c, index + 1, visited)
                        visited.remove((next_r, next_c))
            return res

        res = False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if word[0] == board[r][c]:
                    visited = set()
                    visited.add((r, c))
                    res |= dfs(r, c, 0, visited)
        return res