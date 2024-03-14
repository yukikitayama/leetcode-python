"""
DFS
  visit cell
  check 8 directions to count mines
    if 0, record "B" and continue recursion
    if more than 0, record digit and end recursion
  edge
    if click is "M", record "X"
"""

from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        directions = [
            (-1, 0), (-1, 1), (0, 1), (1, 1),
            (1, 0), (1, -1), (0, -1), (-1, -1)
        ]

        visited = set()

        def dfs(r, c):

            # Edge
            if board[r][c] == "M":
                board[r][c] = "X"
                return

            if board[r][c] == "E":

                mines = 0
                # Count mines
                for offset_r, offset_c in directions:
                    next_r = r + offset_r
                    next_c = c + offset_c

                    if 0 <= next_r < len(board) and 0 <= next_c < len(board[0]):
                        if board[next_r][next_c] == "M":
                            mines += 1

                if mines > 0:
                    board[r][c] = str(mines)
                # Empty without adjacent mines
                else:
                    board[r][c] = "B"

                    # Recursively visit adjacent
                    for offset_r, offset_c in directions:
                        next_r = r + offset_r
                        next_c = c + offset_c

                        if 0 <= next_r < len(board) and 0 <= next_c < len(board[0]) and (next_r, next_c) not in visited:
                            dfs(next_r, next_c)

        visited.add((click[0], click[1]))
        dfs(click[0], click[1])

        return board