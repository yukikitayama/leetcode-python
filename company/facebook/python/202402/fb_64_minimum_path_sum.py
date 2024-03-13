"""
Bottom up DP with S: O(MN)

Optimize space
  current value depends on only two previous states
  current row only depends on previous row
    can reduct O(MN) to O(N)
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [0] * len(grid[0])

        for r in range(len(grid)):
            for c in range(len(grid[0])):

                if r == 0:
                    if c == 0:
                        dp[c] = grid[r][c]
                    else:
                        dp[c] = grid[r][c] + dp[c - 1]

                else:
                    if c == 0:
                        dp[c] = grid[r][c] + dp[c]
                    else:
                        dp[c] = grid[r][c] + min(dp[c - 1], dp[c])

            # print(f"r: {r}, dp: {dp}")

        return dp[-1]

    def minPathSum1(self, grid: List[List[int]]) -> int:

        dp = [[0] * len(grid[0]) for _ in range(len(grid))]

        # Base
        dp[0][0] = grid[0][0]

        # Base
        for r in range(1, len(grid)):
            dp[r][0] = dp[r - 1][0] + grid[r][0]

        # Base
        for c in range(1, len(grid[0])):
            dp[0][c] = dp[0][c - 1] + grid[0][c]

        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])):
                dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]

        # for row in dp:
        #     print(row)

        return dp[-1][-1]
