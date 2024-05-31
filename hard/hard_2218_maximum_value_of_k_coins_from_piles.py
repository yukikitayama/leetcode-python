"""
dp(i, num_coin)
  returns total with at most num_coin number of coins from the left i piles
    e.g. dp(4, 7) means total value with 7 coins from the first 4 piles from the left
  base case
    i is 0, no piles, so no coin gained, regardless of num_coin
"""

from typing import List
import functools


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:

        @functools.cache
        def dp(index, coin):

            # Base case: No more pile
            if index == 0:
                return 0

            ans = 0
            curr_sum = 0

            for curr_coin in range(min(len(piles[index - 1]), coin) + 1):

                if curr_coin > 0:
                    curr_sum += piles[index - 1][curr_coin - 1]

                ans = max(
                    ans,
                    dp(index - 1, coin - curr_coin) + curr_sum
                )

            return ans

        return dp(len(piles), k)
