import functools


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        MOD = 10 ** 9 + 7

        @functools.lru_cache(maxsize=None)
        def dp(i):

            # Base
            if i == 0:
                return 1

            ans = 0
            if i - zero >= 0:
                ans += dp(i - zero)
            if i - one >= 0:
                ans += dp(i - one)
            return ans % MOD

        return sum(dp(i) for i in range(low, high + 1)) % MOD

    def countGoodStrings1(self, low: int, high: int, zero: int, one: int) -> int:

        # high + 1 because of creating space for empty string
        dp = [0] * (high + 1)

        # Base case: there is only one way to create length 0 empty string
        dp[0] = 1

        for i in range(1, len(dp)):

            # Avoid index out of bound
            if i - zero >= 0:
                dp[i] += dp[i - zero]

            # Avoid index out of bound
            if i - one >= 0:
                dp[i] += dp[i - one]

            dp[i] %= (10 ** 9 + 7)

        return sum(dp[low:high + 1]) % (10 ** 9 + 7)