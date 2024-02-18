"""
Bottom up dp
DFS
Backtracking
"""

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        # Edge case
        if obstacleGrid[0][0] == 1 or obstacleGrid[n - 1][m - 1] == 1:
            return 0

        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1

        for r in range(1, n):
            if obstacleGrid[r][0] == 0:
                dp[r][0] = dp[r - 1][0]

        for c in range(1, m):
            if obstacleGrid[0][c] == 0:
                dp[0][c] = dp[0][c - 1]

        for r in range(1, n):
            for c in range(1, m):
                if obstacleGrid[r][c] == 0:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        # for row in dp:
        # print(row)

        return dp[n - 1][m - 1]
