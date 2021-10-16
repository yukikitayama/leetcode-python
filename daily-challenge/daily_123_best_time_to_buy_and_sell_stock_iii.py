"""
- left_profits[i] represents max profits so far by prices[:i]
- right_profits[i] represents max profits so far by prices[i:]
- max profit is max(left_profits[i], right_profits[i + 1])
  - so left and right prices won't overlap,
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        left_min = prices[0]
        right_max = prices[-1]

        length = len(prices)

        left_profits = [0] * length
        right_profits = [0] * (length + 1)

        for l in range(1, length):
            left_profits[l] = max(left_profits[l - 1], prices[l] - left_min)
            left_min = min(left_min, prices[l])

            r = length - 1 - l
            right_profits[r] = max(right_profits[r + 1], right_max - prices[r])
            right_max = max(right_max, prices[r])

        print(f'prices: {prices}')
        print(f'left_profits: {left_profits}')
        print(f'right_profits: {right_profits}')

        max_profit = 0
        for i in range(length):
            max_profit = max(max_profit, left_profits[i] + right_profits[i + 1])

        return max_profit


prices = [3,3,5,0,0,3,1,4]
print(Solution().maxProfit(prices))

