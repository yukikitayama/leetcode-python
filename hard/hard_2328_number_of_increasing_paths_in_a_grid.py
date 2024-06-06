"""
Longer path contains smaller path which is also part of answer

dp[i][j]
  represents number of path that end at each cell
  the number of paths ending at grid[i + 1][j] should be incremented by grid[i][j],
    because every path that ends at grid[i][j] can be extended to grid[i + 1][j]
  If we sort these cells by value, then traverse over them from the smallest
"""

from typing import List


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        val_r_c_list = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                val_r_c_list.append([grid[r][c], r, c])
        val_r_c_list.sort()

        # Base case: all cells are one as one length array
        dp = [[1] * len(grid[0]) for _ in range(len(grid))]

        for val, r, c in val_r_c_list:

            for offset_r, offset_c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_r = r + offset_r
                next_c = c + offset_c
                if 0 <= next_r < len(grid) and 0 <= next_c < len(grid[0]):
                    if grid[next_r][next_c] > val:
                        dp[next_r][next_c] += dp[r][c]
                        dp[next_r][next_c] %= MOD

        ans = 0

        for row in dp:
            ans += sum(row)
            ans %= MOD

        return ans