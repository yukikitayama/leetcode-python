import functools


class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n

        prev_2 = 1
        prev_1 = 2

        for i in range(3, n + 1):
            curr = prev_1 + prev_2
            prev_2 = prev_1
            prev_1 = curr

        return curr

    def climbStairs1(self, n: int) -> int:

        @functools.cache
        def dp(n):
            if n <= 0:
                return 0
            elif n <= 2:
                return n

            return dp(n - 1) + dp(n - 2)

        return dp(n)