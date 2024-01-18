import functools


class Solution:
    def climbStairs(self, n: int) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(curr):
            # print(curr)

            if curr > n:
                return 0

            if curr == n:
                return 1

            # add two results because it seeks the number of distinct ways, not maximum
            return dp(curr + 1) + dp(curr + 2)

        return dp(0)


if __name__ == "__main__":
    n = 2
    # n = 3
    print(Solution().climbStairs(n))
