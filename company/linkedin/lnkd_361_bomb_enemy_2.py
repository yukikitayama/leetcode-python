"""
"""


from typing import List


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        rows, cols = len(grid), len(grid[0])

        ans = 0
        row_hits = 0
        col_hits = [0] * cols

        for row in range(rows):
            for col in range(cols):

                # Reset the hits on the row
                if col == 0 or grid[row][col - 1] == 'W':
                    row_hits = 0
                    for k in range(col, cols):
                        if grid[row][k] == 'W':
                            break
                        elif grid[row][k] == 'E':
                            row_hits += 1

                # Reset the hist on the column
                if row == 0 or grid[row - 1][col] == 'W':
                    col_hits[col] = 0
                    for k in range(row, rows):
                        if grid[k][col] == 'W':
                            break
                        elif grid[k][col] == 'E':
                            col_hits[col] += 1

                if grid[row][col] == '0':
                    total_hits = row_hits + col_hits[col]
                    ans = max(ans, total_hits)

        return ans


grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
print(Solution().maxKilledEnemies(grid))

