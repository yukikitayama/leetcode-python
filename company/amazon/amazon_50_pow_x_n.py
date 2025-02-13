"""
1024 = 2 * 2 * ... * 2 (10 times)

x ** n
  T: O(N)

x**n = x * x ** (n - 1)

1024 = 2 ** 2 * 2 ** 2 ... 2 ** 2 (5 times)
T: O(N / 2)

x**n = (x * x)**(n / 2) if even
x**n = (x * x)**((n - 1) / 2) * x if odd
  e.g., n = 5

2**100 = (2 * 2)**50 = 4**50
4**50 = (4 * 4)**25 = 16**25
16**25 = 16 * (16 * 16)**12 = 16 * 256**12

If negative
  x**(n) = 1/ (x**-n) if n < 0


if n >= 2
  return x ** 2
if n == 1
  return x
recurrence transition
  return x ** 2 * recursion(x, n)
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:

        def recursion(x, n):

            if n == 1:
                return x

            if n == 0:
                return 1

            if n < 0:
                return 1 / recursion(x, -n)

            if n % 2 == 0:
                return recursion(x * x, n // 2)
            elif n % 2 != 0:
                return x * recursion(x * x, (n - 1) // 2)

        return recursion(x, n)