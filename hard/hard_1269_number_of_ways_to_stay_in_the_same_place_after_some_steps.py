import functools


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7
        arrLen = min(arrLen, steps)
        dp = [[0] * (steps + 1) for _ in range(arrLen)]

        # Base case
        dp[0][0] = 1

        for remain in range(1, steps + 1):
            for index in range(arrLen - 1, -1, -1):

                # Stay
                ans = dp[index][remain - 1]

                # Left
                if index > 0:
                    ans += dp[index - 1][remain - 1]
                    ans %= MOD

                # Right
                if index < arrLen - 1:
                    ans += dp[index + 1][remain - 1]
                    ans %= MOD

                dp[index][remain] = ans

        return dp[0][steps]

    def numWays1(self, steps: int, arrLen: int) -> int:

        MOD = 10 ** 9 + 7

        @functools.cache
        def dp(index, remain):

            # Base case: out of bound
            if index < 0 or index >= arrLen:
                return 0

            # Base case: no more step needed
            if remain == 0:
                if index == 0:
                    return 1
                else:
                    return 0

            res = 0

            # Move right
            res += dp(index + 1, remain - 1)
            res %= MOD

            # Move left
            res += dp(index - 1, remain - 1)
            res %= MOD

            # Stay
            res += dp(index, remain - 1)
            res %= MOD

            return res

        return dp(0, steps)