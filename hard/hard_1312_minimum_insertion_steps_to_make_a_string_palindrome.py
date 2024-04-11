"""
Ans
  Length of the longest common subsequence (LCS) in given string and reverse string
  s length minus length of LCS is the answer, because characters not in the LCS needs to be added to form palindrome.
"""

import functools


class Solution:
    def minInsertions(self, s: str) -> int:
        dp = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]

        for r in range(len(dp)):
            for c in range(len(dp[0])):
                if r == 0 or c == 0:
                    continue

                if s[r - 1] == s[-(c + 1 - 1)]:
                    dp[r][c] = 1 + dp[r - 1][c - 1]

                else:
                    dp[r][c] = max(
                        dp[r - 1][c],
                        dp[r][c - 1]
                    )

        return len(s) - dp[-1][-1]

    def minInsertions1(self, s: str) -> int:

        @functools.lru_cache(maxsize=None)
        def dp(i, j):

            # Base: if we exhaust either, no more to form palindrome
            if i < 0 or j < 0:
                return 0

            if s[i] == s[-(j + 1)]:
                return 1 + dp(i - 1, j - 1)
            else:
                return max(
                    dp(i - 1, j),
                    dp(i, j - 1)
                )

        len_lcs = dp(len(s) - 1, len(s) - 1)

        return len(s) - len_lcs
