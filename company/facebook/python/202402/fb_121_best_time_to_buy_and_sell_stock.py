from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        ans = 0

        for i in range(1, len(prices)):
            if prices[i] > min_so_far:
                ans = max(prices[i] - min_so_far, ans)

            min_so_far = min(min_so_far, prices[i])

        return ans
