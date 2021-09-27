"""
- DP cumsum from origin to end.
- Reset to 0 when it has obstacle
- Return matrix[row - 1][col - 1]
- Initialize DP array with 0
  - base case dp[0][0] is 1
- Check if the right and down are 0 cell
"""


from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstaclesGrid: List[List[int]]) -> int:
        m = len(obstaclesGrid)
        n = len(obstaclesGrid[0])

        # Edge case
        if obstaclesGrid[0][0] == 1:
            return 0

        # Base case
        # Start
        obstaclesGrid[0][0] = 1

        # Row
        for i in range(1, m):
            if obstaclesGrid[i][0] == 0 and obstaclesGrid[i - 1][0] == 1:
                obstaclesGrid[i][0] = 1
            else:
                obstaclesGrid[i][0] = 0

        # Column
        for i in range(1, n):
            if obstaclesGrid[0][i] == 0 and obstaclesGrid[0][i - 1] == 1:
                obstaclesGrid[0][i] = 1
            else:
                obstaclesGrid[0][i] = 0

        # Traverse
        for i in range(1, m):
            for j in range(1, n):
                if obstaclesGrid[i][j] == 0:
                    obstaclesGrid[i][j] = obstaclesGrid[i - 1][j] + obstaclesGrid[i][j - 1]
                else:
                    obstaclesGrid[i][j] = 0

        # [print(row) for row in obstaclesGrid]

        return obstaclesGrid[m - 1][n - 1]


obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
obstacleGrid = [[0,1],[0,0]]
print(Solution().uniquePathsWithObstacles(obstacleGrid))


