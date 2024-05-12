from typing import List
import functools


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        dp = [float("inf")] * 3

        # Base case
        for c in range(3):
            dp[c] = costs[0][c]

        # State transition
        for r in range(1, len(costs)):
            next_dp = [None] * 3

            next_dp[0] = costs[r][0] + min(dp[1], dp[2])
            next_dp[1] = costs[r][1] + min(dp[0], dp[2])
            next_dp[2] = costs[r][2] + min(dp[0], dp[1])

            dp = next_dp[:]

        return min(dp)

    def minCost3(self, costs: List[List[int]]) -> int:

        dp = [[float("inf")] * 3 for _ in range(len(costs))]

        # Base case
        for c in range(3):
            dp[0][c] = costs[0][c]

        # State transition
        for r in range(1, len(costs)):
            dp[r][0] = costs[r][0] + min(dp[r - 1][1], dp[r - 1][2])
            dp[r][1] = costs[r][1] + min(dp[r - 1][0], dp[r - 1][2])
            dp[r][2] = costs[r][2] + min(dp[r - 1][0], dp[r - 1][1])

        return min(dp[-1])

    def minCost2(self, costs: List[List[int]]) -> int:

        @functools.cache
        def dp(r, c):

            if r < 0:
                return 0

            ans = costs[r][c]

            if c == 0:
                ans += min(dp(r - 1, 1), dp(r - 1, 2))
            elif c == 1:
                ans += min(dp(r - 1, 0), dp(r - 1, 2))
            elif c == 2:
                ans += min(dp(r - 1, 0), dp(r - 1, 1))

            return ans

        return min(
            dp(len(costs) - 1, 0),
            dp(len(costs) - 1, 1),
            dp(len(costs) - 1, 2)
        )

    def minCost1(self, costs: List[List[int]]) -> int:

        @functools.cache
        def dp(house, color):

            if house < 0:
                return 0

            ans = float("inf")

            if color == 0:
                ans = min(
                    ans,
                    costs[house][color] + dp(house - 1, 1),
                    costs[house][color] + dp(house - 1, 2)
                )

            elif color == 1:
                ans = min(
                    ans,
                    costs[house][color] + dp(house - 1, 0),
                    costs[house][color] + dp(house - 1, 2)
                )

            elif color == 2:
                ans = min(
                    ans,
                    costs[house][color] + dp(house - 1, 0),
                    costs[house][color] + dp(house - 1, 1)
                )

            return ans

        return min(
            dp(len(costs) - 1, 0),
            dp(len(costs) - 1, 1),
            dp(len(costs) - 1, 2)
        )
