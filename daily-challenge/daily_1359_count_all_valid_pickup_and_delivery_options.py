"""
- greedy
- math
"""


import functools


class Solution:
    def countOrders(self, n: int) -> int:

        @functools.cache
        def total_ways(unpicked, undelivered):

            if not unpicked and not undelivered:
                return 1

            if unpicked < 0 or undelivered < 0 or undelivered < unpicked:
                return 0

            ans = unpicked * total_ways(unpicked - 1, undelivered)
            ans %= MOD

            ans += (undelivered - unpicked) * total_ways(unpicked, undelivered - 1)
            ans %= MOD

            return ans

        MOD = 1_000_000_007

        return total_ways(n, n)


if __name__ == '__main__':
    n = 2
    print(Solution().countOrders(n))
