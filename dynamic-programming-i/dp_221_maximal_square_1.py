from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        # print('matrix')
        # [print(row) for row in matrix]

        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0

        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        maxsqlen = 0

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i - 1][j - 1] == '1':
                    # min because minimum element obstructs the formation of a square
                    # Plus one because matrix[i - 1][j - 1] itself is also one small square
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    # Update max length of a square so far
                    maxsqlen = max(maxsqlen, dp[i][j])

        # print(f'dp')
        # [print(row) for row in dp]

        return maxsqlen ** 2


matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
print(Solution().maximalSquare(matrix))
