from typing import List
from itertools import accumulate
from functools import lru_cache


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        print(f'piles: {piles}')

        N = len(piles)

        # tmp = piles
        # cumsum = []
        # for i in accumulate(reversed(tmp)):
        #     cumsum.append(i)
        # cumsum = list(reversed(cumsum))
        # print(f'cumsum: {cumsum}')

        # Make cumulative sum from the end of piles to the beginning,
        # so result is from the biggest to smallest
        # e.g. N: 5, range(3, -1, -1): (3, 2, 1, 0)
        for i in range(N - 2, -1, -1):
            # print(f'i: {i}')
            piles[i] += piles[i + 1]

        print(f'piles: {piles}')

        # maxsize=None makes the cache grow indefinitely
        @lru_cache(maxsize=None)
        def dp(i, m):


piles = [2,7,9,4,4]
print(Solution().stoneGameII(piles))
