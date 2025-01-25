from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_count = [0] * len(grid)
        col_count = [0] * len(grid[0])

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    row_count[r] += 1
                    col_count[c] += 1

        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    if row_count[r] > 1 or col_count[c] > 1:
                        ans += 1

        return ans