"""
Offset
  (0, 1)
  (1, 0)
  (0, -1)
  (-1, 0)
Times
  m - 1
  n - 1
  m - 1
  n - 2
  m - 2

DFS
  not visited the visited
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # # Edge
        # if len(matrix) == 1 and len(matrix[0]) == 1:
        #     return [matrix[0][0]]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visited = set()
        ans = []

        def dfs(r, c, i):

            if (r, c) in visited:
                return

            if not (0 <= r < len(matrix) and 0 <= c < len(matrix[0])):
                return

            visited.add((r, c))
            ans.append(matrix[r][c])

            offset_r, offset_c = directions[i]
            next_r = r + offset_r
            next_c = c + offset_c

            # Change direction
            if next_r < 0 or len(matrix) == next_r or next_c < 0 or len(matrix[0]) == next_c or (
            next_r, next_c) in visited:
                offset_r, offset_c = directions[(i + 1) % 4]
                next_r = r + offset_r
                next_c = c + offset_c
                dfs(next_r, next_c, (i + 1) % 4)

            else:
                dfs(next_r, next_c, i)

        dfs(0, 0, 0)

        return ans
