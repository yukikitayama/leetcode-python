import functools


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base
        for r in range(1, m + 1):
            dp[r][0] = dp[r - 1][0] + ord(s1[r - 1])
        for c in range(1, n + 1):
            dp[0][c] = dp[0][c - 1] + ord(s2[c - 1])

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if s1[r - 1] == s2[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    dp[r][c] = min(
                        ord(s1[r - 1]) + dp[r - 1][c],
                        ord(s2[c - 1]) + dp[r][c - 1]
                    )

        # for row in dp:
        #     print(row)

        return dp[-1][-1]

    def minimumDeleteSum2(self, s1: str, s2: str) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(p1, p2):

            # Base
            if p1 < 0 and p2 < 0:
                return 0

            # Base
            if p1 < 0:
                return ord(s2[p2]) + dp(p1, p2 - 1)

            # Base
            elif p2 < 0:
                return ord(s1[p1]) + dp(p1 - 1, p2)

            # Recurrence
            if s1[p1] == s2[p2]:
                return dp(p1 - 1, p2 - 1)

            else:
                return min(
                    dp(p1 - 1, p2) + ord(s1[p1]),
                    dp(p1, p2 - 1) + ord(s2[p2])
                )

        return dp(len(s1) - 1, len(s2) - 1)

    def minimumDeleteSum1(self, s1: str, s2: str) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(p1, p2):

            # Base
            if p1 < 0:
                ans = 0
                while p2 >= 0:
                    ans += ord(s2[p2])
                    p2 -= 1
                return ans

            elif p2 < 0:
                ans = 0
                while p1 >= 0:
                    ans += ord(s1[p1])
                    p1 -= 1
                return ans

            # Recurrence
            if s1[p1] == s2[p2]:
                return dp(p1 - 1, p2 - 1)

            else:
                return min(
                    dp(p1 - 1, p2) + ord(s1[p1]),
                    dp(p1, p2 - 1) + ord(s2[p2])
                )

        return dp(len(s1) - 1, len(s2) - 1)
