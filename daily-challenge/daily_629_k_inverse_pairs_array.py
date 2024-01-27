"""
n, 3, k: 2

[3, 1, 2]

create array
swap
check if k inverse pairs

When a number is shifted y times to the left from the ordered array,
y numbers smaller than it lie to the right, so there is y inverse pairs
"""

import functools


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(n, k):

            # Base, no array element, no pair
            if n == 0:
                return 0

            # Base, only ascending array
            if k == 0:
                return 1

            ans = 0

            for i in range(min(k, n - 1) + 1):
                ans = (ans + dp(n - 1, k - i)) % (10 ** 9 + 7)

            return ans

        return dp(n, k)




