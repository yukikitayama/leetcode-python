"""
Should have more 1s at left to have big numbers
Count 1s in rows and columns
  rows: [2, 2, 2]
  cols: [2, 1, 2, 1]

"""

from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:

        # Make 1st column 1 for each row
        col_zero = [0] * len(grid[0])

        for r in range(len(grid)):

            flip = False

            for c in range(len(grid[0])):

                if grid[r][0] == 0:
                    flip = True

                if flip:
                    grid[r][c] = 1 if grid[r][c] == 0 else 0

                if grid[r][c] == 0:
                    col_zero[c] += 1

        # for row in grid:
        #     print(row)
        # print()
        # print(col_zero)

        # Flip if more 0s for each column
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if col_zero[c] > len(grid) // 2:
                    grid[r][c] = 1 if grid[r][c] == 0 else 0

        # Accumulate the sum
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    ans += 2 ** (len(grid[0]) - c - 1)

        return ans