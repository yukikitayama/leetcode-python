from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]

        ans = 0

        for i in range(1, len(prices)):
            curr = prices[i]

            if curr > min_so_far:
                profit = curr - min_so_far
                ans += profit
                min_so_far = curr

            elif curr < min_so_far:
                min_so_far = curr

        return ans


"""
Complexity
- Time is O(n) by letting n the length of prices
- Space is O(1)
"""


prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]
prices = [7,6,4,3,1]
print(Solution().maxProfit(prices))
