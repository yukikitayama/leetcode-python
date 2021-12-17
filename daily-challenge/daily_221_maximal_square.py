"""
- dp[i][j] represents the side length of the max square whose bottom right corner is
  the (i, j) cell.
"""


from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1) ]

        max_side = 0

        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):

                # This is wrong because when matrix is 0, no need to update dp
                # When matrix[row - 1][col - 1] is '0', side is 0, because current cell doesn't allow to make a side
                # but if min(3 things) is 1 for example, dp[row][col] is 1, but it should be 0
                # dp[row][col] = int(matrix[row - 1][col - 1]) + min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1])

                if matrix[row - 1][col - 1] == '1':
                    dp[row][col] = 1 + min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1])
                max_side = max(max_side, dp[row][col])

        # [print(row) for row in dp]

        return max_side ** 2


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix = [
    ['0', '1', '1', '1', '0'],
    ['1', '1', '1', '1', '0'],
    ['0', '1', '1', '1', '1'],
    ['0', '1', '1', '1', '1'],
    ['0', '0', '1', '1', '1'],
]
matrix = [
    ["1","0","1","1","0","1"],
    ["1","1","1","1","1","1"],
    ["0","1","1","0","1","1"],
    ["1","1","1","0","1","0"],
    ["0","1","1","1","1","1"],
    ["1","1","0","1","1","1"]
]
# 4
print(Solution().maximalSquare(matrix))




