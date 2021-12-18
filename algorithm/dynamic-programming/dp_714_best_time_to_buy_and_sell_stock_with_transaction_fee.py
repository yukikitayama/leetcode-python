from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = -prices[0]

        print(f'cash: {cash}, hold: {hold}, prices[0]: {prices[0]}')

        for i in range(1, len(prices)):
            # Track max cash so far
            cash = max(cash, prices[i] + hold - fee)
            # Track max hold so far
            hold = max(hold, cash - prices[i])

            print(f'  cash: {cash}, hold: {hold}, prices[i]: {prices[i]}')

        return cash


prices = [1,3,2,8,4,9]
fee = 2
print(Solution().maxProfit(prices, fee))
