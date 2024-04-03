"""
DP
"""

from typing import List


class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        dp = [[float("inf")] * 2 for _ in range(len(regular))]

        ans = []

        # Base
        dp[0][0] = regular[0]
        dp[0][1] = expressCost + express[0]
        ans.append(min(dp[0]))

        for i in range(1, len(regular)):
            dp[i][0] = min(dp[i - 1][0] + regular[i], dp[i - 1][1] + regular[i])
            dp[i][1] = min(dp[i - 1][0] + expressCost + express[i], dp[i - 1][1] + express[i])

            ans.append(min(dp[i]))

        # for row in dp:
        #     print(row)

        return ans
