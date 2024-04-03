from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # First cell
                if r == 0 and c == 0:
                    continue

                # First row
                if r == 0 and c > 0:
                    grid[r][c] = grid[r][c] + grid[r][c - 1]

                # First column
                elif r > 0 and c == 0:
                    grid[r][c] = grid[r][c] + grid[r - 1][c]

                # Other cells
                else:
                    grid[r][c] = grid[r][c] + min(grid[r - 1][c], grid[r][c - 1])

        # for row in grid:
        #     print(row)

        return grid[-1][-1]
