"""
- We can reach ith step by
  - one step from (i - 1)th step
  - two step from (i - 2)th step
- total number of ways to reach ith step is
  - number of ways to reach (i - 1)th step plus number of ways to reach (i - 2)th step
- dp[i] represents the number of ways to reach ith step
  - dp[i] = dp[i - 1] + dp[i - 2]
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)

        # Base case
        # 0th step is 1 because we always start from 0th step, so there's only one way to be there
        dp[0] = 1
        # 1th step is only taking one step from 0th step starting position
        dp[1] = 1
        for i in range(2, len(dp)):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]


print(Solution().climbStairs(2))
print(Solution().climbStairs(3))





