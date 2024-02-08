"""
eg.
  row
    0, 0, 1, 2, 1, 0, 1, 2, 2
  col
    0, 1, 0, 0, 1, 2, 2, 1, 2
  sum
    0, 1, 1, 2, 2, 2, 3, 3, 3
  7: (2, 0), 5: (1, 1), 3: (0, 2)

Collect from bottom left to top right direction
  start as leftmost column and bottom row
  if start row + col is odd, reverse the order, use queue.appendleft
    (0, 0)
    (1, 0) r, odd
    (2, 0)
    (2, 1) r, odd
    (2, 2)
"""

from typing import List
import collections


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])

        start_row_col = []
        for row in range(n):
            start_row_col.append((row, 0))
        for col in range(1, m):
            start_row_col.append((n - 1, col))

        # print(start_row_col)

        ans = []
        for r, c in start_row_col:

            # print(r, c)

            queue = collections.deque()

            while 0 <= r < n and 0 <= c < m:

                if (r + c) % 2 == 0:
                    queue.append(mat[r][c])
                else:
                    queue.appendleft(mat[r][c])

                c += 1
                r -= 1

            # print(queue)

            ans.extend(queue)

        return ans
