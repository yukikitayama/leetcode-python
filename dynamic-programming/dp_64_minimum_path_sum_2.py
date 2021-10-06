"""
- Initialize dp matrix to 0s with the same size as grid
- dp[i][j] represents minimum sum from the origin
- Base case dp[0][0] = grid[0][0]
- Iterate row in grid rows
  - Iterate col in grid cols
    - Skip row == 0, and col == 0
    - If row == 0, dp[0][col] = grid[0][col] + dp[0][col - 1]
    - If col == 0, dp[row][0] = grid[row][0] + dp[row][col - 1]
    - Else, dp[row][col] = grid[row][col] + min(dp[row - 1][col], dp[row][col - 1])
- return dp[end row][end col]

Test
grid = [
[1,3,1],
[1,5,1],
[4,2,1]
]
Before iteration
dp:
[1, 0, 0]
[0, 0, 0]
[0, 0, 0]
After iteration
dp:
[1, 4, 5]
[2, 7, 6]
[6, 8, 7]
"""


from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    dp[row][col] = grid[row][col]
                elif row == 0:
                    dp[row][col] = grid[row][col] + dp[row][col - 1]
                elif col == 0:
                    dp[row][col] = grid[row][col] + dp[row - 1][col]
                else:
                    dp[row][col] = grid[row][col] + min(dp[row - 1][col], dp[row][col - 1])

        return dp[m - 1][n - 1]


grid = [[1,3,1],[1,5,1],[4,2,1]]
grid = [[1,2,3],[4,5,6]]
print(Solution().minPathSum(grid))
