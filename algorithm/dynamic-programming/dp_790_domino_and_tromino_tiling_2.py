"""
n: 1
  ans: 1
n: 2
  ans: 2
n: 3
  ans: 3 (domino) + 2 (tromino)
n: 4
  ans: n: 1 + n: 3, n: 2 + n: 2, n: 3 + n: 1

dp(n):
  base case, n is 1, 2, or 3

  ans = 0
  for i in range(1, n):
    ans += dp(i) + dp(n - i)
"""

import functools


class Solution:
    def numTilings(self, n: int) -> int:

        MOD = 10 ** 9 + 7

        @functools.cache
        def f(n):

            # Base case
            if n <= 0:
                return 0
            if n == 1:
                return 1
            # 2 vertical bars and 2 horizontal bars
            if n == 2:
                return 2

            return (f(n - 1) + f(n - 2) + 2 * p(n - 1)) % MOD

        @functools.cache
        def p(n):

            # Base case
            # Tromino always cover at least 2 columns
            if n <= 1:
                return 0
            # Tromino always cover at least 2 columns
            if n == 2:
                # Doesn't count symmetry here, because we will multiply 2 in a different place
                return 1

            return (f(n - 2) + p(n - 1)) % MOD

        return f(n)

    def numTilings1(self, n: int) -> int:

        @functools.cache
        def dp(n):

            # Base case
            if n <= 0:
                return 0
            elif n <= 2:
                return n
            elif n == 3:
                return 5

            ans = 0

            for i in range(1, n):
                ans += (dp(i) + dp(n - i)) % (10 ** 9 + 7)

            return ans

        return dp(n)