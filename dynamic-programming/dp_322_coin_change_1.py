"""
Top down dynamic programming
- Define F(S) as minimum number of coins needed to make amount 2 by using denomination coins array
-
"""


from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        print(f'coins: {coins}, amount: {amount}')

        if amount < 1:
            return 0

        count = [0] * amount

        return self.coin_change(coins, amount, count)

    def coin_change(self, coins: List[int], rem: int, count: List[int]) -> int:

        print(f'rem: {rem}, count: {count}')

        if rem < 0:
            return -1

        if rem == 0:
            return 0

        # Use result from memoization
        if count[rem - 1] != 0:
            return count[rem - 1]

        min = float('inf')

        for coin in coins:
            # rem: 11, coin: 1
            #   rem: 10, coin: 1,
            #     continue until rem becomes 0
            res = self.coin_change(coins, rem - coin, count)

            # res < 0 means exceeding amount, so it's bad
            # res < min?
            if res >= 0 and res < min:
                min = 1 + res
                print(f'  min: {min}')

        count[rem - 1] = -1 if min == float('inf') else min

        print(f'rem: {rem}, min: {min}, count[rem - 1]: {count[rem - 1]}')

        return count[rem - 1]



coins = [1,2,5]
amount = 11
print(Solution().coinChange(coins, amount))
