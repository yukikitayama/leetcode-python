from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0

        dp = [0] * (cols + 1)
        maxsqlen = 0
        prev = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                # dp[j] is updated in each iteration
                # dp[j] is from dp[j - 1]: left, prev: top left, and dp[j]: top
                # In the next iteration, top becomes top left, but because we update dp[j] in place
                # prev from previous iteration dp[j] is not previous row dp, rather current row dp
                # but dp[j] needs to be updated from the previous row, so
                # set dp[j] to temporary variable and assign it to prev at the end of each iteration
                # to save the previous row data.
                temp = dp[j]

                # -1 because dp starts from index 1 but matrix needs to start from index 0
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(dp[j - 1], prev, dp[j]) + 1
                    maxsqlen = max(maxsqlen, dp[j])

                else:
                    dp[j] = 0

                prev = temp

        return maxsqlen ** 2


"""
prev: 0
i: 1, j: 1, temp: dp[j] = 0
matrix[0][0]: 1, dp[j - 1]: 0, prev: 0, 

Bottom up dynamic programming with optimized space
Time: Let m be the number of rows and n be the number of columns. O(nm)
Space: O(n) because dp array is one dimensional
"""


matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
print(Solution().maximalSquare(matrix))
