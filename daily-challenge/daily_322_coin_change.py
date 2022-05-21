"""
- bottom-up dp, because combination sum can be reused
"""


from typing import List
import math
import functools


# Bottom up DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # +1 because of 0 base case
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        coins.sort()

        for i in range(1, amount + 1):

            for coin in coins:

                if i >= coin:

                    dp[i] = min(dp[i], dp[i - coin] + 1)

                else:
                    break

        return dp[-1] if dp[-1] != float('inf') else -1


# Top down DP
class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @functools.lru_cache(None)
        def dp(amount):

            if amount == 0:
                return 0

            ans = math.inf

            for coin in coins:

                if amount >= coin:

                    # +1 because of using 1 coin here
                    ans = min(ans, dp(amount - coin) + 1)

            return ans

        ans = dp(amount)

        return ans if ans != math.inf else -1


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    print(Solution().coinChange(coins, amount))
