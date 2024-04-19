from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(r, c):
            grid[r][c] = "-1"

            for offset_r, offset_c in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_r = r + offset_r
                next_c = c + offset_c
                if 0 <= next_r < len(grid) and 0 <= next_c < len(grid[0]) and grid[next_r][next_c] == "1":
                    dfs(next_r, next_c)

        ans = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r, c)
                    ans += 1

        return ans
