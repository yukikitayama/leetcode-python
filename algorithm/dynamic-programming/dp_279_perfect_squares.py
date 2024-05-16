"""
eg
  n: 0, 0
  n: 1, 1, 1
  n: 2, 1 + 1 = 2, 2
  n: 3, 1 + 1 + 1 = 3, 3
  n: 4, 4, 1
  n: 5, 1 + 4 = 5, 2

dp
  base case
    if n <= 3, return n
  Recurrence state transition
    ans: big number
    for each perfect square number
       ans = min of ans or 1 + dp(current number - a perfect square number)
    return ans
Perfect square numbers
  if current number is 18
    1**2, 2**2, 3**2, 4**2
  before recursion, pre-make a list of perfect square numbers
"""

import functools


class Solution:
    def numSquares(self, n: int) -> int:

        perfect_squares = []
        candidate = 1
        while candidate ** 2 <= n:
            perfect_squares.append(candidate ** 2)
            candidate += 1

        # print(perfect_squares)

        @functools.cache
        def dp(n):

            # Base case
            if n <= 0:
                return 0

            elif n <= 3:
                return n

            ans = float("inf")

            for perfect_square in perfect_squares:

                if n - perfect_square >= 0:
                    ans = min(
                        ans,
                        1 + dp(n - perfect_square)
                    )

            return ans

        return dp(n)
