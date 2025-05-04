"""
number of elements in grid
  area of x, y
sum of maximum of each row
  area of x, z
sum of maximum of each column
  area of y, z
"""

from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans = sum(map(max, grid))
        ans += sum(map(max, zip(*grid)))
        ans += sum(num > 0 for row in grid for num in row)
        return ans

    def projectionArea1(self, grid: List[List[int]]) -> int:
        ans = 0

        # Area of x, y
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > 0:
                    ans += 1

        # Area of z, x
        for row in grid:
            ans += max(row)

        # Area of y, z
        for c in range(len(grid[0])):
            col_max = 0
            for r in range(len(grid)):
                col_max = max(col_max, grid[r][c])
            ans += col_max

        return ans