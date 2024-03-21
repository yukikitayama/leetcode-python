import functools


class Solution:
    def fib(self, n: int) -> int:
        @functools.lru_cache(maxsize=None)
        def dp(n):
            if n <= 1:
                return n

            return dp(n - 1) + dp(n - 2)

        return dp(n)