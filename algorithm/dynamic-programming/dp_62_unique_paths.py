class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """S: O(N)"""
        dp = [1] * n

        # print(f"Base: {dp}")

        for r in range(1, m):
            for c in range(n):
                if c == 0:
                    dp[c] = dp[c]
                else:
                    dp[c] = dp[c] + dp[c - 1]

            # print(dp)

        return dp[-1]

    def uniquePaths1(self, m: int, n: int) -> int:
        """S: O(MN)"""
        dp = [[0] * n for _ in range(m)]

        # Base
        for r in range(m):
            dp[r][0] = 1
        for c in range(n):
            dp[0][c] = 1

        # DP
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[-1][-1]