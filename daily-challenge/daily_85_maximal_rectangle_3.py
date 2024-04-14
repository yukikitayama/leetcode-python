from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ans = 0

        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):

                if matrix[r][c] == "0":
                    continue

                # Only consider current is "1" cases
                else:
                    # else 1 because current is "1"
                    dp[r][c] = dp[r][c - 1] + 1 if c > 0 else 1
                    width = dp[r][c]

                    # Check rows above from current row
                    for prev_r in range(r, -1, -1):
                        width = min(width, dp[prev_r][c])
                        # +1 for being inclusive
                        ans = max(ans, width * (r - prev_r + 1))

        return ans
