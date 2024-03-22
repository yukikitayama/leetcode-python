import functools


class Solution:
    def tribonacci(self, n: int) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(n):
            if n == 0:
                return 0
            elif n <= 2:
                return 1
            else:
                return dp(n - 1) + dp(n - 2) + dp(n - 3)

        return dp(n)
