"""
"""


from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        # dp i + 1, j + 1 corresponds to matrix i, j
        dp = [0] * (n + 1)

        # Square side length
        max_side = 0
        prev = 0

        for row in range(m):
            for col in range(n):
                temp = dp[col + 1]
                if matrix[row][col] == '1':
                    # prev: top left, dp[col + 1]: top, dp[col]: left
                    dp[col + 1] = 1 + min(prev, dp[col + 1], dp[col])
                    max_side = max(max_side, dp[col + 1])

                # If current cell in matrix is 0, there's no any size of square possible
                # So reset it to 0
                else:
                    dp[col + 1] = 0

                prev = temp

        return max_side ** 2


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# matrix = [["0","1"],["1","0"]]
print(Solution().maximalSquare(matrix))


