from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        held = float('-inf')
        sold = float('-inf')
        rest = 0

        for i in range(len(prices)):
            tmp_held = held
            tmp_sold = sold
            held = max(held, rest - prices[i])
            sold = tmp_held + prices[i]
            rest = max(rest, tmp_sold)

        return max(sold, rest)


prices = [1, 2, 3, 0, 2]
prices = [1]
print(Solution().maxProfit(prices))
