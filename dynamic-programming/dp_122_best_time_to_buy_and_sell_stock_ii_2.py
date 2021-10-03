from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0

        for i in range(1, len(prices)):
            prev_price = prices[i - 1]
            curr_price = prices[i]
            profit = curr_price - prev_price
            if profit > 0:
                ans += profit

        return ans


prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]
prices = [7,6,4,3,1]
print(Solution().maxProfit(prices))


