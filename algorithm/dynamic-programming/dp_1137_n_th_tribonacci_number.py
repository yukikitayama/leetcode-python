"""
dp(i)
  i is n
  base case,
    If i = 0, 0
    If i == 1 or 2, 1
  otherwise
    ans = dp(i - 1) + dp(i - 2) + dp(i - 3)
  return
    T_i
"""

import functools


class Solution:
    def tribonacci(self, n: int) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(i):

            if i == 0:
                return 0
            if i == 1 or i == 2:
                return 1

            return dp(i - 1) + dp(i - 2) + dp(i - 3)

        return dp(n)


if __name__ == "__main__":
    n = 25
    print(Solution().tribonacci(n))
