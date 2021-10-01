"""
Bottom up dynamic programming
"""


from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # amount + 1 because we need space for amount is 0 as base case
        dp = [float('inf')] * (amount + 1)
        # 0 amount does not need any amount of coins
        dp[0] = 0

        for coin in coins:

            # print(f'coin: {coin}')

            for x in range(coin, amount + 1):

                dp[x] = min(dp[x], dp[x - coin] + 1)
                # print(f'  x: {x}, dp: {dp}')

        return dp[amount] if dp[amount] != float('inf') else -1


coins = [1,2,5]
amount = 11
print(Solution().coinChange(coins, amount))
