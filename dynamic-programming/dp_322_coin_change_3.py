"""
Top down dp

- Recursively pick coin from coins and add up
  - Increment number of coins every time entering recursion
  - Stop recursion when the total sum is equal to amount
- Recursion returns the number of coins
- Recursion input is current sum, current number of coins

coints: [1, 2, 5]
amount: 11
- 11
  - 10 (1)
    - 9 (1)
    - 8 (2)
    - 5 (5)
  - 9 (2)
    - 8 (1)
    - 7 (2)
    - 4 (5)
  - 6 (5)
    - 5 (1)
    - 4 (2)
    - 1 (5)
"""


from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount < 1:
            return 0

        # +1 for 0 amount
        dp = [0] * amount

        return self.coin_change(coins, amount, dp)

    def coin_change(self, coins, amount, dp):

        if amount < 0:
            return -1

        if amount == 0:
            return 0

        # We initialized dp array with 0s, so if it's not zero, there was update
        if dp[amount - 1] != 0:
            return dp[amount - 1]

        min_count_so_far = float('inf')
        for coin in coins:
            remaining = amount - coin
            result = self.coin_change(coins, remaining, dp)
            if result >= 0:
                # +1 because we use one coin from coins in the above for loop
                min_count_so_far = min(min_count_so_far, result + 1)

        dp[amount - 1] = -1 if min_count_so_far == float('inf') else min_count_so_far

        # dp array length is amount. The last element represents the minimum number of coints to make the amount
        # so return element at amount - 1 for 0 index
        return dp[amount - 1]


"""
coin: 1, amount: 1, remaining: 0, coin_change() returns 0, result: 0, min_count_so_far: 1
  because 
  
amount: 3
dp: [0, 0, 0]

"""


coins = [1,2,5]
amount = 11
print(Solution().coinChange(coins, amount))


