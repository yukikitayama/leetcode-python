from typing import List
import functools


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]

        for left in range(len(s) - 1, -1, -1):
            dp[left][left] = 1
            for right in range(left + 1, len(s)):

                if s[left] == s[right]:
                    # Left iterates from right to left, so left + 1 is already computed
                    # Right iterates after left, so right - 1 is already compued
                    dp[left][right] = dp[left + 1][right - 1] + 2

                else:
                    dp[left][right] = max(dp[left + 1][right], dp[left][right - 1])

        for row in dp:
            print(row)

        return dp[0][len(s) - 1]

    def longestPalindromeSubseq1(self, s: str) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(l, r):
            if l == r:
                return 1
            elif l > r:
                return 0

            if s[l] == s[r]:
                return 2 + dp(l + 1, r - 1)
            else:
                return max(
                    dp(l, r - 1),
                    dp(l + 1, r)
                )

        return dp(0, len(s) - 1)
