"""
- Make dp matrix
- dp[i][j] represents the side length of the maximum square whose bottom right corner is
  the cell with index (i, j) in the original matrix.
  - max square side length up to index (i, j)
"""


from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        # dp i + 1, j + 1 corresponds to matrix i, j
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Square side length
        max_side = 0

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == '1':
                    dp[row + 1][col + 1] = 1 + min(dp[row + 1][col], dp[row][col + 1], dp[row][col])
                    max_side = max(max_side, dp[row + 1][col + 1])

        return max_side ** 2


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix = [["0","1"],["1","0"]]
print(Solution().maximalSquare(matrix))


