"""
edge case
  if click is on M
    Make it X
DFS or BFS
  visit E
    initialize mine counter 0
    Check neighbor (8 directions)
      if neighbor is mine
        increment mine counter
    If counter is zero
      mark B
    else
      mark string of counter
    visit neighbor
      if current is B

[(0, 1)used, (1, 0)used, (2, 1), (1, 2), (0, 0)used B, (0, 0)already B]

B  B  E

B  B  E

E  E  E
"""

from typing import List
import collections


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board

        queue = collections.deque()
        queue.append((click[0], click[1]))

        while queue:

            for _ in range(len(queue)):

                r, c = queue.popleft()

                # print(r, c)
                if board[r][c] != "E":
                    continue

                counter = 0

                for dr, dc in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                        if board[nr][nc] == "M":
                            counter += 1

                if counter == 0:
                    board[r][c] = "B"
                else:
                    board[r][c] = str(counter)

                if board[r][c] == "B":
                    for dr, dc in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == "E":
                            queue.append((nr, nc))

        return board

