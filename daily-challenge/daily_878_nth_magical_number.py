"""
Example
Input: n = 1, a = 2, b = 3
Output: 2
2 is divisible by 2

Input: n = 4, a = 2, b = 3
Output: 6
n: 1 = 2
n: 2 = 3
n: 3 = 4
n: 4 = 6

Input: n = 5, a = 2, b = 4
Output: 10
n: 1 = 2, 2 divisible by 2
n: 2 = 4, 4 divisible by 2 and 4
n: 3 = 6, 6 divisible by 2
n: 4 = 8, 8 divisible by 2 and 4
n: 5 = 10, 10 divisible by 2

Input: n = 3, a = 6, b = 4
Output: 8
n: 1 = 4, divisible by 4,
n: 2 = 6, divisible by 6
n: 3 = 8, divisible by 4

L: least common multiple of A and B
- e.g. a: 2, b: 4, L: 2

If X <= L is magical, then X + L is magical
- e.g. A: 4, B: 8, L: 4, X: 4 <= L and magical, X + L: 8, also magical

There are M = L/A + L/B - 1 magical numbers less than or equal to L
- L/A are divisible by A
- L/B are divisible by B
- 1 is divisible by both

N = M * q + r
- r < M
- The first L * q numbers contain M * q magical numbers
- We want to find r more magical ones within the next (L * q + 1, L * q + 2, ...)
"""


import math


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7

        L = abs(a * b) // math.gcd(a, b)
        M = L // a + L // b - 1
        q, r = divmod(n, M)

        if r == 0:
            return q * L % MOD

        heads = [a, b]
        for _ in range(r - 1):
            if heads[0] <= heads[1]:
                heads[0] += a
            else:
                heads[1] += b

        return (q * L + min(heads)) % MOD


n = 1
a = 2
b = 3
n = 4
a = 2
b = 3
print(Solution().nthMagicalNumber(n, a, b))
