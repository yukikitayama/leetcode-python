"""
- If obstacleGrid[0][0] is 1, return 0
- If obstacleGrid[end row][end col] is 1, return 0
- dp[i][j] represents the number of ways from origin to reach (i, j)
- dp size is one length bigger than the grid
  - first row and first col are extra
  - dp i + 1 and j + 1 correspond to the grid i and j
- Initialize dp to 0
- Iterate row from 1 to end row
  - Iterate col from 1 to end col
    - If row is 1 and col is 1, dp[row][col] = 1
    - else if the grid[row - 1][col - 1] is 0, dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
    - else if the grid[row - 1][col - 1] is 1, dp[row][col] = 0
"""


from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # Edge case
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        # Dynamic programming array one length larger than input grid
        # dp row + 1 and col + 1 correspond to the grid row and col
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # range end +1 because bp array is one length larger
        for row in range(1, m + 1):
            for col in range(1, n + 1):

                # Base case
                if row == 1 and col == 1:
                    dp[row][col] = 1

                # No obstacle
                elif obstacleGrid[row - 1][col - 1] == 0:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

                # Reset dp array because there's obstacle
                elif obstacleGrid[row - 1][col - 1] == 1:
                    dp[row][col] = 0

        # See dp array after iteration
        # [print(row) for row in dp]

        # Not m - 1 and n - 1 because dp array is one length larger
        return dp[m][n]


"""
Idea
- Bottom up dynamic programming
- dp[i + 1][j + 1] represents the number of ways to reach from the input grid origin to grid (i, j)
- Use dynamic programming array to avoid modifying the input grid array in place.

Complexity
- Time: O(mn) by letting m be the number of rows and n be the number of columns
- Space: O(mn)
"""


"""
Test
obstacleGrid = [
[0,0,0],
[0,1,0],
[0,0,0]
]
dp = [
[0, 0, 0, 0], 
[0, 1, 0, 0], 
[0, 0, 0, 0], 
[0, 0, 0, 0]
]
row: 1, col: 2
row: 2, col: 2
"""

obstacleGrid = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
print(Solution().uniquePathsWithObstacles(obstacleGrid))



