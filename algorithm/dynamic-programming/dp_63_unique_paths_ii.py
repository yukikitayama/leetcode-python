"""
DP matrix initialize with 0
Base
  first column and first row
    fill 1 until it sees grid 1,
    after grid 1, no update
Recurrence
  dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
  if grid[r][c] is 1, no update
Return
  dp[-1][-1]
Edge
  start and end is obstacle 1
"""

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """S: O(N)"""
        dp = [0] * len(obstacleGrid[0])

        if obstacleGrid[0][0] == 0:
            dp[0] = 1
        else:
            dp[0] = 0

        for c in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][c] == 0:
                dp[c] = dp[c - 1]

        # print(dp)

        for r in range(1, len(obstacleGrid)):
            for c in range(len(obstacleGrid[0])):
                if obstacleGrid[r][c] == 0:
                    if c == 0:
                        dp[c] = dp[c]
                    else:
                        dp[c] = dp[c] + dp[c - 1]
                else:
                    dp[c] = 0

            # print(dp)

        return dp[-1]

    def uniquePathsWithObstacles1(self, obstacleGrid: List[List[int]]) -> int:
        """S: O(MN)"""
        dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]

        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        else:
            dp[0][0] = 0

        for r in range(1, len(obstacleGrid)):
            if obstacleGrid[r][0] == 0:
                dp[r][0] = dp[r - 1][0]

        for c in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][c] == 0:
                dp[0][c] = dp[0][c - 1]

        for r in range(1, len(obstacleGrid)):
            for c in range(1, len(obstacleGrid[0])):
                if obstacleGrid[r][c] == 0:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[-1][-1]
