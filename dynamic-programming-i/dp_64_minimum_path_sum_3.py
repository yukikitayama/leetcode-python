"""
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

        # dp = [[0] * n for _ in range(m)]
        dp = [0] * n

        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    dp[col] = grid[row][col]
                elif row == 0:
                    dp[col] = grid[row][col] + dp[col - 1]
                elif col == 0:
                    dp[col] = grid[row][col] + dp[col]
                else:
                    dp[col] = grid[row][col] + min(dp[col], dp[col - 1])

            # print(f'dp: {dp}')

        return dp[n - 1]


# grid = [[1,3,1],[1,5,1],[4,2,1]]
grid = [[1,2,3],[4,5,6]]
print(Solution().minPathSum(grid))
