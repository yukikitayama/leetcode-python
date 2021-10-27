"""
- brute force
- TLE
"""


from typing import List


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        def kill_enemies(row, col):
            enemy_count = 0
            # [(going up), (going down)]
            row_ranges = [range(row - 1, -1, -1), range(row + 1, rows)]
            for row_range in row_ranges:
                for r in row_range:
                    # Wall block the bomb
                    if grid[r][col] == 'W':
                        break
                    elif grid[r][col] == 'E':
                        enemy_count += 1

            col_ranges = [range(col - 1, -1, -1), range(col + 1, cols)]
            for col_range in col_ranges:
                for c in col_range:
                    if grid[row][c] == 'W':
                        break
                    elif grid[row][c] == 'E':
                        enemy_count += 1

            return enemy_count

        ans = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '0':
                    ans = max(ans, kill_enemies(row, col))
        return ans



grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
print(Solution().maxKilledEnemies(grid))

