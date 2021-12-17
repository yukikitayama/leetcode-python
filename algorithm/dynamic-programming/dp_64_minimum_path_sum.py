"""
Result
- Start: 8:31
- End: 8:35
- Solved: 1
- Saw solution: 0
- Optimized: 1
"""


from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]

        # Base case
        dp[0][0] = grid[0][0]
        for i in range(1, len(dp)):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, len(dp[0])):
            dp[0][i] = dp[0][i - 1] + grid[0][i]

        # [print(row) for row in dp]

        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                dp[row][col] = grid[row][col] + min(dp[row - 1][col], dp[row][col - 1])

        return dp[-1][-1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(Solution().minPathSum(grid))

