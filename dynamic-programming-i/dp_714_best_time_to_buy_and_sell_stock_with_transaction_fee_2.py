from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # cash is the max profit we have if we have no stock at the end of ith day
        # hold is the max profit we have if we hold stock at the end of the ith day
        cash = 0
        hold = -prices[0]

        for i in range(1, len(prices)):

            # print(f'i: {i}, prices[i]: {prices[i]}')
            # print(f'  start of {i}th day: cash: {cash}, hold: {hold}')

            cash = max(cash, hold + prices[i] - fee)
            # We can do below because we can buy again after we sell the stock
            hold = max(hold, cash - prices[i])

            # print(f'  end of {i}th day: cash: {cash}, hold: {hold}')

        return cash


prices = [1,3,2,8,4,9]
fee = 2
print(Solution().maxProfit(prices, fee))


