"""
- Initialize dp array to 0 because we haven't chosen coin
- Set dp[0] to 1 because there's one combination to make 0 which is don't choose coins
- Iterate each coin in coins
  - Iterate current amount from coin to amount
    - Subtract coin from the current amount by i - coin
    - find the number of ways without current coin by dp[i - coin]
    - We have a new number of ways by using coin to dp[i - coin] ways to
    - increment dp[i] with dp[i - coin]
    - There's no index out of boundary because current amount starts from current coin and end with amount
"""


from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)

        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

            # print(f'  dp: {dp}')

        # print(f'dp: {dp}')

        return dp[amount]


"""
Test
amount: 5
coins: [1, 2, 5]
dp: [1, 0, 0, 0, 0, 0]
coin: 1
  i: 1, dp[i - coin]: dp[1 - 1] = 1, dp[1]: 1
  i: 2, dp[i - coin]: dp[2 - 1] = d[1] = 1, dp[2]: 1
  ...
coin: 2,
  i: 2, dp[i - coin]: dp[2 - 2] = dp[0] = 1, dp[2]: 1 + 1 = 2
"""


amount = 5
coins = [1, 2, 5]
print(Solution().change(amount, coins))


