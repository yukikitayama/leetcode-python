"""
Reject below
- Initialize ans
- for each perfect square from small to large
  - Initialize current count to 0
  - large is a number smaller than the given n
  - if n - current perfect square is bigger than 0
    - recursive to n - current perfect square
      - When the remaining is 0, return 1
      - Increment current count
  - ans = min(ans, current count)
- return ans

Algorithm
- bottom up dp
"""


import math


class Solution:
    def numSquares(self, n):
        square_nums = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]

        print(f'square_nums: {square_nums}, n: {n}, int(math.sqrt(n)): {int(math.sqrt(n))}')

        dp = [float('inf')] * (n + 1)

        dp[0] = 0

        for i in range(1, n + 1):

            for square in square_nums:

                print(f'  i: {i}, square: {square}')

                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)

                print(f'    dp: {dp}')

        return dp[-1]


print(Solution().numSquares(9))

