"""
2^10
  2^9 * 2 = 2^(n - 1) * 2
    2^8 * 2 * 2 = 2^(n - 2)
      ...
n times recursion

(-2)**4
  (-2) * (-2)**3

2**(-4)
  1/2 * 2(-3)
    1/2 * 1/2 * 2(-2)


2^10
  = (2 * 2)^9 = 4**9
    = (4 * 4) ** 5 = (2 ** 2 * 2 ** 2) ** 5
      = (2 ** 4 * 2 ** 4) * 1

2**4
  2 * 2**3
    2 * 2 * 2**2
      2 * 2 * 2 * 2**1
        2 * 2 * 2 * 2 * 2**0

2**4
  (2 * 2) * 2**2

2**8
  (2 * 2) * 2**6 = 4 * (2**2)**4

4**2
  (4 * 4) ** 0


Instead of original x, use squared x as based to seep up
But reduce power

recursion(x, n)
  recursion(x * x, n -)

x^n depends on previous result
Recursion

When x is negative
  -2**0 = 1
  -2**1 = -2
  -2**2 = 4
  -2**3 = -8
    if power is odd, result is negative
    if even, result is positive

Ans
  Use formula: x**n = (x**2) ** (n / 2)

  2**4 = (2**2) ** (4 / 2)
  2**5 = (2**2) ** (1 + 4/2) = 2 * (2**2) ** (4 / 2)

  When power is 1
    base * recursion(base * base, 0) = base * 1
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:

        def recursion(base, power):

            # Base to terminate
            if power == 0:
                return 1

            # Pass once
            if power < 0:
                return 1 / recursion(base, -power)

            # Recursion
            # return base * recursion(base, power - base)

            if power % 2 == 0:
                return recursion(base * base, power // 2)
            elif power % 2 != 0:
                return base * recursion(base * base, (power - 1) // 2)

        return recursion(x, n)
