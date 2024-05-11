"""
Like backtracking

amount = 5, coins = [1,2,5]
when remaining is 1, we know there is only one way
when remaining is 0,
  return 1 as one way to make up
dp(remain - coin)

return dp(amount)
"""

from typing import List
import functools


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in range(len(coins) - 1, -1, -1):
            for remaining in range(coins[c], amount + 1):
                dp[remaining] += dp[remaining - coins[c]]

        return dp[amount]

    def change2(self, amount: int, coins: List[int]) -> int:

        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        # Base case: if remaining amount is 0, regardless of coin, form one way
        for i in range(len(coins)):
            dp[i][0] = 1

        # State transition
        for c in range(len(coins) - 1, -1, -1):
            for remaining in range(1, amount + 1):

                if remaining >= coins[c]:
                    # Use current coin or skip
                    dp[c][remaining] = dp[c][remaining - coins[c]] + dp[c + 1][remaining]

                # Try another coint
                elif remaining < coins[c]:
                    dp[c][remaining] = dp[c + 1][remaining]

        # for row in dp:
        #     print(row)

        return dp[0][amount]

    def change1(self, amount: int, coins: List[int]) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(remaining, index):

            if remaining == 0:
                return 1

            elif remaining < 0:
                return 0

            ans = 0

            for i in range(index, len(coins)):
                ans += dp(remaining - coins[i], i)

            return ans

        return dp(amount, 0)
