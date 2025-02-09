from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(r, c):
            grid[r][c] = "0"
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_r = r + dr
                next_c = c + dc
                if 0 <= next_r < len(grid) and 0 <= next_c < len(grid[0]):
                    if grid[next_r][next_c] == "1":
                        dfs(next_r, next_c)

        ans = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r, c)
                    ans += 1

        return ans