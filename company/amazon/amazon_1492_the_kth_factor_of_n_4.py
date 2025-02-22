"""
https://leetcode.com/problems/the-kth-factor-of-n/solutions/959372/7-line-java-o-sqrt-n-time-o-1-space-not-a-typical-explanation/

If n is 12
  divisors: 1, 2, 3, 4, 6, 12
  1 * 12,
  2 * 6,
  3 * 4
  sqrt(12) = 3.46..
  If we think in pair, when x is divisor of n, y = n / x is also divisor
    and it's okay only upto square root of n
"""

import math


class Solution:
    def kthFactor(self, n: int, k: int) -> int:

        x = 1
        while x < math.sqrt(n):
            if n % x == 0:
                k -= 1
                if k == 0:
                    return x
            x += 1

        x = int(math.sqrt(n))
        while x > 0:
            y = n // x
            if n % y == 0:
                k -= 1
                if k == 0:
                    return y
            x -= 1

        return -1
