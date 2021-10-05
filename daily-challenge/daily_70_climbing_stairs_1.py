"""
n: 1
1 step

n: 2
1 step + 1 step
2 step

n: 3
1 step + 1 step + 1 step
1 step + 2 step
2 step + 1 step

n: 4
1, 1, 1, 1
1, 1, 2
1, 2, 1
2, 1, 1
2, 2

dp[i] represents the number of distinct ways to reach i step
dp[0]: 1
dp[1]: 1
dp[2]: dp[1] + dp[0]
dp[3]:
"""


class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}

        def climb_stairs(i, n, memo):
            if i in memo:
                return memo[i]

            if i > n:
                return 0

            if i == n:
                return 1

            memo[i] = climb_stairs(i + 1, n, memo) + climb_stairs(i + 2, n, memo)

            return memo[i]

        return climb_stairs(0, n, memo)


print(Solution().climbStairs(2))
print(Solution().climbStairs(3))





