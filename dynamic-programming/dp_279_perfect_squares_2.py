"""
"""


import math


class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i**2 for i in range(0, int(math.sqrt(n)) + 1)]

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, len(dp)):
            for square in square_nums:
                # It's not continue, but break because square is coming in an ascending order
                if square > i:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[-1]


"""
O(n * sqrt(n)) for a nested for loop
"""


# Least number of perfect square numbers that sum to n
# 2 = 1 + 1
# print(Solution().numSquares(2))

print(Solution().numSquares(6))  # 1 + 1 + 4 = 6, so needs 3 perfect square numbers
# print(Solution().numSquares(12))  # 4 + 4 + 4 = 6, so needs 3 perfect square numbers

