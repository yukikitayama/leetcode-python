"""
DP
- Cumsum from start to end


DFS
- neighbors only (row + 1, col) and (row, col + 1)
- clear visited set to find another unique path
-

"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Any location in the 2d map has at least one possibility to reach the end
        # so base case of DP is 1
        dp = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        # [print(row) for row in dp]

        return dp[m - 1][n - 1]


print(Solution().uniquePaths(3, 7))
print(Solution().uniquePaths(3, 2))
print(Solution().uniquePaths(7, 3))
print(Solution().uniquePaths(3, 3))

