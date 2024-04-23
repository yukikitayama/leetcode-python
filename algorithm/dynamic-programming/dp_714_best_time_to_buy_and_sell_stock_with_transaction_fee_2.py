"""
dp[i] represents the max profit from the first i days
State transition

"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = -prices[0]
        free = 0

        for i in range(1, len(prices)):
            tmp_hold = hold
            hold = max(hold, free - prices[i])
            free = max(free, tmp_hold + prices[i] - fee)

        return free

    def maxProfit1(self, prices: List[int], fee: int) -> int:
        hold = [0] * len(prices)
        free = [0] * len(prices)

        # Base case
        hold[0] = -prices[0]

        # State transition
        for i in range(1, len(prices)):
            hold[i] = max(hold[i - 1], free[i - 1] - prices[i])
            free[i] = max(free[i - 1], hold[i - 1] + prices[i] - fee)

            # print(hold)
            # print(free)

        return free[-1]
