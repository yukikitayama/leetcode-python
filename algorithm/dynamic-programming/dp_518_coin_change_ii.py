from typing import List
import functools


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(amount, coins):

            if amount == 0:
                return 1

            # If there's no list of coins, we cannot make combination
            if amount < 0 or len(coins) == 0:
                return 0

            # Each recursion consider whether one coin from the end is used or not to decrement amount
            return dp(amount - coins[-1], coins) + dp(amount, coins[:-1])

        return dp(amount, tuple(coins))


if __name__ == '__main__':
    amount = 5
    coins = [1,2,5]
    print(Solution().change(amount, coins))
