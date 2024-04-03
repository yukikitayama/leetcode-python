from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 1:
            return matrix[0][0]

        dp = matrix[0]

        for r in range(1, len(matrix)):
            curr = []
            for c in range(len(matrix[0])):
                if c == 0:
                    curr.append(matrix[r][c] + min(dp[c], dp[c + 1]))
                elif 0 < c < len(matrix[0]) - 1:
                    curr.append(matrix[r][c] + min(dp[c - 1], dp[c], dp[c + 1]))
                else:
                    curr.append(matrix[r][c] + min(dp[c - 1], dp[c]))
            dp = curr[:]

        return min(dp)