from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = float('-inf')
        sold = float('-inf')
        rest = 0

        for i in range(len(prices)):
            prev_hold = hold
            prev_sold = sold

            hold = max(hold, rest - prices[i])
            sold = prev_hold + prices[i]
            rest = max(rest, prev_sold)

        return max(sold, rest)


prices = [1, 2, 3, 0, 2]
prices = [1]
print(Solution().maxProfit(prices))

