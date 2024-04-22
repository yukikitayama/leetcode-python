from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold = float("-inf")
        hold = float("-inf")
        reset = 0

        for i in range(len(prices)):
            prev_sold = sold

            # Sell
            sold = hold + prices[i]

            # Buy
            # max(do nothing, buy)
            hold = max(hold, reset - prices[i])

            # Cooldown
            # max(do nothing, sell)
            reset = max(reset, prev_sold)

        return max(sold, reset)