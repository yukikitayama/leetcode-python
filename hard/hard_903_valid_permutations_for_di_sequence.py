import functools


class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10 ** 9 + 7

        @functools.cache
        def dp(i, j):
            if i == 0:
                return 1

            # s[i] needs to be smaller than s[i - 1]
            elif s[i - 1] == 'D':
                # e.g. i: 3, j: 0
                return sum(dp(i - 1, k) for k in range(j, i)) % MOD

            elif s[i - 1] == 'I':
                # s[i] needs to be smaller than s[i]
                return sum(dp(i - 1, k) for k in range(j)) % MOD

        return sum(dp(len(s), j) for j in range(len(s) + 1)) % MOD
