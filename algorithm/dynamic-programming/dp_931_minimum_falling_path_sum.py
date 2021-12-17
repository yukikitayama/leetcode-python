"""
Result
- Start: 8:44
- End: 8:49
- Solved: 1
- Saw solution: 0
- Optimized: 1
"""


from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        # Base case
        for i in range(len(dp[0])):
            dp[0][i] = matrix[0][i]

        # [print(row) for row in dp]

        for row in range(1, len(dp)):
            for col in range(len(dp[0])):
                if col == 0:
                    dp[row][col] = matrix[row][col] + min(dp[row - 1][col], dp[row - 1][col + 1])
                elif col == len(dp[0]) - 1:
                    dp[row][col] = matrix[row][col] + min(dp[row - 1][col], dp[row - 1][col - 1])
                else:
                    dp[row][col] = matrix[row][col] + min(dp[row - 1][col], dp[row - 1][col - 1], dp[row - 1][col + 1])

        # [print(row) for row in dp]

        return min(dp[-1])


matrix = [[2,1,3],[6,5,4],[7,8,9]]
# 13
print(Solution().minFallingPathSum(matrix))
