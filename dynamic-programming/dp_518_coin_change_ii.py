from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i] is the number of combinations to make i amount
        # +1 for extra 0 amount space
        # Initialize with 0 because with no coins, no combinations
        dp = [0] * (amount + 1)

        # Base case, when amount is 0, there's only one combination; to take zero coins
        dp[0] = 1

        for coin in coins:

            for i in range(coin, len(dp)):

                dp[i] += dp[i - coin]

        return dp[-1]


amount = 5
coins = [1,2,5]
print(Solution().change(amount, coins))

