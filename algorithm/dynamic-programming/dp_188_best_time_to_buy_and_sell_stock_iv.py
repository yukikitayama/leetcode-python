"""
States
- Index to array
- How many transactions left
- Holding a stock or not

"""


from typing import List
import functools


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(index, remaining_transaction, holding):
            if remaining_transaction == 0:
                return 0
            if index == len(prices):
                return 0

            do_nothing = dp(index + 1, remaining_transaction, holding)

            if holding:
                # Sell
                do_something = prices[index] + dp(index + 1, remaining_transaction - 1, 0)
            else:
                # Buy
                do_something = -prices[index] + dp(index + 1, remaining_transaction, 1)

            return max(do_nothing, do_something)

        return dp(0, k, 0)


k = 2
prices = [3,2,6,5,0,3]
print(Solution().maxProfit(k, prices))
