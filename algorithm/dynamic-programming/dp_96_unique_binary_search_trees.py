class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)

        # 1 because at multiplication we wanna have no effect
        dp[0] = 1

        dp[1] = 1

        for root in range(2, n + 1):
            for i in range(1, root + 1):
                # print(f"root: {root}, i - 1: {i - 1}, root - i: {root - i}")

                dp[root] += dp[i - 1] * dp[root - i]

        return dp[n]
