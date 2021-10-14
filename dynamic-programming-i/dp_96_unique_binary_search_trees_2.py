"""
G(n) = sigma i=1 to n of F(i, n)
G(0): 1
G(1):1
F(i, n) = sigma i=1 to n of G(i - 1) * G(n - i)
so G(n) = sigma i=1 to n of G(i - 1) * G(n - i)
"""


class Solution:
    def numTrees(self, n: int) -> int:
        G = [0] * (n + 1)
        G[0], G[1] = 1, 1

        for N in range(2, n + 1):
            for i in range(1, N + 1):
                G[N] += G[i - 1] * G[N - i]

        return G[n]


print()