"""
- dp[0]: 1
- dp[1]: 1
- dp[2]: dp[1] + dp[0]
- dp[3]: dp[2] + dp[1]


"""

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        # print(f'dp: {dp}')

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # print(f'  dp: {dp}')

        return dp[-1]


print(Solution().climbStairs(2))
print(Solution().climbStairs(3))


