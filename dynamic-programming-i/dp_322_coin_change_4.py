"""
"""


from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount < 1:
            return 0

        # Make a dp array. We wanna get a minimum number so
        # we initialize with a big number
        # +1 because we wanna space of 0 amount
        # dp[i] represent the minimum number of coins needed to make amount i
        dp = [float('inf')] * (amount + 1)

        # Base case
        # amount 0 minimum number of coin needed is 0
        dp[0] = 0

        for i in range(1, len(dp)):
            for coin in coins:
                remaining = i - coin

                # If remaining is negative, it cannot make the amount
                if remaining < 0:
                    continue

                # e.g. i: 1, coin: 1, remaining: 0
                # i: 2,
                #  coin: 1, remaining: 1, dp[1]: 1, dp[2] = min(large value, dp[1] + 1) = min(large, 2)
                # +1 because we currently need to add one coin
                #  coin: 2, remaining: 0, dp[0]: 0, dp[2] = min(2, 0 + 1)
                # dp[2]: 1, end
                dp[i] = min(dp[i], dp[remaining] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1

"""

"""


coins = [1,2,5]
amount = 11
coins = [2]
amount = 3
coins = [1]
amount = 1
print(Solution().coinChange(coins, amount))


