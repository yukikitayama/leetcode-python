"""
Iterate board
  if current character equal to first character of word
    BFS
      next visiting cell is the next character of word
      use visited set to avoid visiting the previous cells
"""

from typing import List
import collections


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def bfs(r, c):
            queue = collections.deque()
            # [(row, col, index in word)]
            queue.append((r, c, 0))
            visited = set()
            visited.add((r, c))

            while queue:

                for _ in range(len(queue)):

                    curr_r, curr_c, curr_i = queue.popleft()

                    if curr_i == len(word) - 1:
                        return True

                    for offset_r, offset_c in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        next_r = curr_r + offset_r
                        next_c = curr_c + offset_c
                        if 0 <= next_r < len(board) and 0 <= next_c < len(board[0]):
                            if (next_r, next_c) not in visited and board[next_r][next_c] == word[curr_i + 1]:
                                queue.append((next_r, next_c, curr_i + 1))
                                visited.add((next_r, next_c))

            return False

        def backtracking(curr_r, curr_c, curr_i, visited):
            if curr_i == len(word) - 1:
                return True

            ans = False
            for offset_r, offset_c in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                next_r = curr_r + offset_r
                next_c = curr_c + offset_c
                if 0 <= next_r < len(board) and 0 <= next_c < len(board[0]):
                    if (next_r, next_c) not in visited and board[next_r][next_c] == word[curr_i + 1]:

                        visited.add((next_r, next_c))
                        if backtracking(next_r, next_c, curr_i + 1, visited):
                            ans = True
                            break

                        # Backtrack
                        visited.discard((next_r, next_c))

            return ans

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if backtracking(r, c, 0, set([(r, c)])):
                        return True

        return False
