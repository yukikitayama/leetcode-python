class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n

        # No use the f_dp[0] for convenience
        f_dp = [0] * (n + 1)
        p_dp = [0] * (n + 1)

        f_dp[1] = 1
        f_dp[2] = 2
        p_dp[2] = 1

        for i in range(3, n + 1):
            f_dp[i] = (f_dp[i - 1] + f_dp[i - 2] + 2 * p_dp[i - 1]) % (10**9 + 7)
            p_dp[i] = (p_dp[i - 1] + f_dp[i - 2]) % (10**9 + 7)

        return f_dp[-1]

