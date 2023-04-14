class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        n = len(s)

        memo = {}

        def lps(l, r):

            if (l, r) in memo:
                return memo[(l, r)]

            if l > r:
                return 0

            if l == r:
                return 1

            if s[l] == s[r]:
                memo[(l, r)] = 2 + lps(l + 1, r - 1)

            else:
                # Either shrink right side, or left side
                memo[(l, r)] = max(lps(l, r - 1), lps(l + 1, r))

            return memo[(l, r)]

        return lps(0, n - 1)


