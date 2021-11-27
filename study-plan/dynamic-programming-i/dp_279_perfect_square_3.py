"""
- dp[0]: 0
- dp[1]
  - i: 1, square: 0, dp[i]: min(dp[i], dp[i - square] + 1) = min(inf, inf) = inf
      i: 1, square: 1, dp[i]: min(dp[i], dp[i - square] + 1) = min(inf, dp[0] + 1) = 1
- dp[2]
  - i: 2, square: 0, dp[2]: min(dp[2], dp[2 - 0]) = inf
      i: 2, square: 1, dp[]
"""


import math


class Solution:
    def numSquares(self, n: int) -> int:
        # Get integers of perfect squares
        square_nums = [i**2 for i in range(0, int(math.sqrt(n)) + 1)]

        # print(f'square_nums: {square_nums}')

        dp = [float('inf')] * (n + 1)

        # We can't choose any perfect square number to make 0
        dp[0] = 0

        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)

        return int(dp[-1])


print(Solution().numSquares(12))
