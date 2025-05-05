import functools


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 1_000_000_007

        @functools.cache
        def p(n):
            if n == 2:
                # Place L, 2 variation can be handle in f()
                return 1
            return (
                # Add 1 horizontal to L
                    p(n - 1)
                    # Add L
                    + f(n - 2)
            ) % MOD

        @functools.cache
        def f(n):
            if n <= 2:
                return n

            return (
                # Add 1 vertical
                    f(n - 1)
                    # Add 2 horizontal
                    + f(n - 2)
                    # Add L, 2 symmetry
                    + 2 * p(n - 1)
            ) % MOD

        return f(n)