import functools


class Solution:
    def tribonacci(self, n: int) -> int:

        @functools.cache
        def dp(n):

            if n == 0:
                return 0
            elif n <= 2:
                return 1

            return dp(n - 1) + dp(n - 2) + dp(n - 3)

        return dp(n)