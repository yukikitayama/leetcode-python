"""
Bottom up DP
  iterate from 2nd row
    dp[r][c] = triangle[r][c] + min(triangle[r - 1][c - 1], triangle[r - 1][c])
    no min if c is 0, just current plus current
    no min if c is last, just current plus previous
  return minimum of the last row
Edge
  1 row
    return the element
"""

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """Without inplace modify, S: O(N)"""
        # Edge
        if len(triangle) == 1:
            return triangle[0][0]

        # Base
        dp = triangle[0]

        for r in range(1, len(triangle)):
            curr = []
            for c in range(r + 1):
                if c == 0:
                    curr.append(dp[c] + triangle[r][c])
                elif c == r:
                    curr.append(dp[c - 1] + triangle[r][c])
                else:
                    curr.append(min(dp[c - 1], dp[c]) + triangle[r][c])
            dp = curr

        return min(dp)

    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        """S: O(MN)"""

        # Edge
        if len(triangle) == 1:
            return triangle[0][0]

        dp = []
        # Base
        dp.append([triangle[0][0]])

        for r in range(1, len(triangle)):
            curr = []
            for c in range(r + 1):
                if c == 0:
                    curr.append(dp[r - 1][c] + triangle[r][c])
                elif c == r:
                    curr.append(dp[r - 1][c - 1] + triangle[r][c])
                else:
                    curr.append(min(dp[r - 1][c - 1], dp[r - 1][c]) + triangle[r][c])
            dp.append(curr)

        # for row in dp:
        #     print(row)

        return min(dp[-1])
