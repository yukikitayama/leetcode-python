"""
Recurrence
  if dp top, top left, left are 1 and if matrix current is 1, current dp can update
Dp is bigger than matrix
  dp contains 0, 1, 2, meaning size of square length
return max so far size**2
"""

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [0] * (len(matrix[0]) + 1)
        side = 0
        prev = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                # Current value will be the prev of the next value
                temp = dp[c + 1]

                if matrix[r][c] == "1":
                    dp[c + 1] = 1 + min(dp[c], dp[c + 1], prev)
                    side = max(side, dp[c + 1])

                else:
                    # If current cell in the matrix is 0, then reset
                    dp[c + 1] = 0

                prev = temp

            print(dp)

        return side * side

    def maximalSquare1(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        size = float("-inf")

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == "1":
                    dp[r + 1][c + 1] = 1 + min(dp[r][c], dp[r][c + 1], dp[r + 1][c])
                    if dp[r + 1][c + 1] > size:
                        size = dp[r + 1][c + 1]

        # for row in dp:
        #     print(row)

        return 0 if size == float("-inf") else size * size