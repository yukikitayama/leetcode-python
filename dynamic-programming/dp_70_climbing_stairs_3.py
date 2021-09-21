class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        # n + 1 because we wanna have space of n: 0
        dp = [0] * (n + 1)
        # No need for dp[0] = 0, because it's initialized with 0
        dp[1] = 1
        dp[2] = 2
        # skip if range start is bigger than or equal to range stop
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


"""
Time complexity
O(n) for one pass

Space complexity
O(n) for dp array of size n 
"""


print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
