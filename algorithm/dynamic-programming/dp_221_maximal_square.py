from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        # +1 to make for loop for the first element easier
        dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        max_len = 0

        for r in range(1, len(dp)):
            for c in range(1, len(dp[0])):

                if matrix[r - 1][c - 1] == "1":
                    dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])

                    max_len = max(max_len, dp[r][c])

        return max_len * max_len


if __name__ == "__main__":
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    print(Solution().maximalSquare(matrix))
