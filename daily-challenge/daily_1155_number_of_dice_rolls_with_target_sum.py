"""
Repeated sub-problems
"""

import functools


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        @functools.lru_cache(maxsize=None)
        def recursion(roll, remain):

            if roll == n and remain == 0:
                return 1

            if roll >= n or remain < 0:
                return 0

            ans = 0

            for i in range(1, k + 1):
                ans = (ans + recursion(roll + 1, remain - i)) % (10 ** 9 + 7)

            return ans

        return recursion(0, target)


if __name__ == "__main__":
    n = 1
    k = 6
    target = 3

    n = 2
    k = 6
    target = 7

    n = 30
    k = 30
    target = 500

    print(Solution().numRollsToTarget(n, k, target))
