"""
- Stack
"""


from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        ans = 0
        # dp is column
        dp = [0] * len(matrix[0])

        # Make histogram for each row
        for i in range(len(matrix)):

            # Update the current histogram from the previous state
            for j in range(len(matrix[0])):
                # Use previous state of column dp to update current state of column dp
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0

            # With current histogram, get area
            ans = max(ans, self.leetcode_84(dp))

        return ans

    def leetcode_84(self, heights):
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)

        while stack[-1] != -1:
            h = heights[stack.pop()]
            w = len(heights) - stack[-1] - 1
            ans = max(ans, h * w)
        return ans

"""
"""

