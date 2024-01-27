"""
Out of the grid boundary
  row < 0 or m <= row
  col < 0 or n <= col

DFS
  track steps
  increment answer integer when steps < maxMove and at the edge of the grid
  allow visit the same cell multiple times

This is dp problem
  We could reach the same position with the same number of remaining moves

dp(i, j, k)
  i: row
  j: col
  k: remaining move
"""

import functools


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(i, j, k):

            # Base case
            if i < 0 or i == m or j < 0 or j == n:
                return 1

            # Base case
            if k == 0:
                return 0

            return (dp(i - 1, j, k - 1) + dp(i + 1, j, k - 1) + dp(i, j - 1, k - 1) + dp(i, j + 1, k - 1)) % (10 ** 9 + 7)

        return dp(startRow, startColumn, maxMove)


if __name__ == "__main__":
    m = 2
    n = 2
    maxMove = 2
    startRow = 0
    startColumn = 0
    # 6

    m = 1
    n = 3
    maxMove = 3
    startRow = 0
    startColumn = 1
    # 12

    print(Solution().findPaths(m, n, maxMove, startRow, startColumn))



