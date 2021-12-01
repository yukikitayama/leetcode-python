"""
Result
- Start: 7:21
- End: 7:22
- Saw solution: 1

Idea
- Dynamic programming
"""


from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ans = 0

        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    continue

                # With above continue, width is only calculated when there's 1
                # if j excludes leftmost column to avoid index out of bound
                width = dp[i][j] = dp[i][j - 1] + 1 if j else 1

                # From bottom to top, check the histograms
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    # (i - k + 1) is height, so using row j (bottom) and k (top)
                    ans = max(ans, width * (i - k + 1))

        return ans


"""
- Let n be row and m be column
- Time is O(n^2 * m) because in the nested for loop, area calculation takes O(n) to iterate each row.
"""

