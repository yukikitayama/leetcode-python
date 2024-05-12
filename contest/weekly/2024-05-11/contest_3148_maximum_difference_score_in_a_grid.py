"""
heap
start from goal

ans
  ans = (b - a) + (c - b) = c - a
  for current end, find minimum start on current top left area
"""

from typing import List


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        ans = float("-inf")

        for r in range(len(grid)):
            for c in range(len(grid[0])):

                if r > 0:
                    prev_row = grid[r - 1][c]
                else:
                    prev_row = float("inf")

                if c > 0:
                    prev_col = grid[r][c - 1]
                else:
                    prev_col = float("inf")

                prev = min(prev_row, prev_col)

                ans = max(
                    ans,
                    grid[r][c] - prev
                )

                grid[r][c] = min(grid[r][c], prev)

        return ans