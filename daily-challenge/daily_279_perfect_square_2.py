"""
2^2 = 4
3^3 = 9
4^4 = 16

12 - 9 = 3

Recursion
  Reduce current num from the largest perfect square
    from 1 to num**2 < current num and reverse
  Return
    length = 1 + recurion(current num - perfect square)
  When current num is 0,
"""


class Solution:
    def numSquares(self, n: int) -> int:

        perfect_squares = [i ** 2 for i in range(1, int(math.sqrt(n)) + 1)]

        @functools.lru_cache(maxsize=None)
        def dp(remaining):

            if remaining == 0:
                return 0

            ans = float("inf")

            for perfect_square in perfect_squares:

                if remaining < perfect_square:
                    break

                ans = min(ans, 1 + dp(remaining - perfect_square))

            return ans

        return dp(n)

