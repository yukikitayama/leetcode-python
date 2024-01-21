"""
top-down dp

(0, 0)
"""

from typing import List
import functools


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(row, col):

            # Base case: col outside boundary
            if col < 0 or len(matrix[0]) <= col:
                return float("inf")

            # Base case: last row
            if row == (len(matrix) - 1):
                return matrix[row][col]

            left = dp(row + 1, col - 1)
            middle = dp(row + 1, col)
            right = dp(row + 1, col + 1)

            return matrix[row][col] + min(left, middle, right)

        ans = float("inf")

        for col in range(len(matrix[0])):
            ans = min(ans, dp(0, col))

        return ans


if __name__ == "__main__":
    matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
    matrix = [[-19, 57], [-40, -5]]
    matrix = [
        [17, 82],
        [1, -44]
    ]  # -27
    print(Solution().minFallingPathSum(matrix))
