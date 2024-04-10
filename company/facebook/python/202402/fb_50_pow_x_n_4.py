"""
x: 2, n: 10
2**10

n is huge
T: O(logN)

2**10
  = (2**2)**10/2 = 4 ** 5
    = 4 * (4 * 4) ** 5//2 =
2**5 = (2**2)**(5 - 1)/2 * 2

2**(-2) = (1/2)**2
if n is 0
  return 1
if n is 1
  return x
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:

        def recursion(x, n):

            # Terminate
            if n == 0:
                return 1
            elif n == 1:
                return x

            # Edge
            elif n < 0:
                return recursion(1/x, -1 * n)

            if n % 2 == 0:
                return recursion(x * x, n / 2)
            elif n % 2 != 0:
                return x * recursion(x * x, (n - 1) / 2)

        return recursion(x, n)