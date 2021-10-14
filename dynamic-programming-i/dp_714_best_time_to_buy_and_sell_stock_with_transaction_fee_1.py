from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Base case for dynamic programming
        cash = 0
        hold = -prices[0]

        for i in range(1, len(prices)):

            # + prics[i] is the amount you get by selling at prices[i]
            cash = max(cash, hold + prices[i] - fee)

            hold = max(hold, cash - prices[i])

        return cash


"""
Algorithm
- Initialize answer: 0
- Iterate each price
  -
"""
prices = [1, 2, 3, 4]
fee = 1
"""
2 - 1 = 1, 3 - 2 = 1, 4 - 3 = 1
2 - 1 - 1 = 0, 3 - 2 - 1 = 0, 4 - 3 - 1 = 0
4 - 1 - 1 = 2
"""
prices = [1, 2, 3, 2, 4]
"""
3 - 1 - 1 = 1, 4 - 2 - 1 = 1, profit: 2
4 - 1 - 1 = 2, profit: 2
As long as price keeps up, hold it. When the next price goes does, sell now
"""

