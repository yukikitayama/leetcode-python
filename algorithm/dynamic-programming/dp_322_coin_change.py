"""
dp(remaining, i)
  base case
    if remaining is 0, return 0 as no number of coins is needed
    if remaining is less than 0, return inf
  Recurrence state transision
    ans = inf
    for coin in coins from i to len
      ans = min(ans, 1 + (remaining - current coin), current coin index)
    if ans is inf, then -1, othewise return ans
"""

from typing import List
import functools


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)

        # Base case
        dp[0] = 0

        for coin in coins:
            for current_amount in range(coin, amount + 1):
                dp[current_amount] = min(
                    dp[current_amount],
                    1 + dp[current_amount - coin]
                )

        return dp[amount] if dp[amount] != float("inf") else -1

    def coinChange2(self, coins: List[int], amount: int) -> int:

        @functools.cache
        def dp(remaining):

            if remaining == 0:
                return 0

            elif remaining < 0:
                return -1

            ans = float("inf")
            for coin in coins:
                res = dp(remaining - coin)
                if res != -1:
                    ans = min(ans, 1 + res)

            return -1 if ans == float("inf") else ans

        return dp(amount)

    def coinChange1(self, coins: List[int], amount: int) -> int:

        @functools.cache
        def dp(remaining, index):

            if remaining == 0:
                return 0
            elif remaining < 0:
                return float("inf")

            ans = float("inf")
            for i in range(index, len(coins)):
                ans = min(
                    ans,
                    1 + dp(remaining - coins[i], i)
                )

            return ans

        ans = float("inf")
        for i in range(len(coins)):
            ans = min(
                ans,
                dp(amount, i)
            )
        return -1 if ans == float("inf") else ans