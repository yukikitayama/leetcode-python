"""
- dp[i][j] represents the number of paths from origin to (i, j)
- Base case dp[0][j] are all 1 and dp[i][0] are all 1
- Iterate row from 1 to m
  - Iterate col from 1 to n
    - dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
- return dp[m - 1][n - 1]
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1 for base case
        dp = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[m - 1][n - 1]


print(Solution().uniquePaths(3, 7))
print(Solution().uniquePaths(3, 2))


