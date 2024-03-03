"""
x**4
x * x * x * x

x**(2 * 4/2) = (x**2) ** 2 = (x * x)

x**5
x**(2 * 4/2 + 1) = (x**2) * 2 * x
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:

        def recursion(base, power):

            if power == 0:
                return 1

            if power < 0:
                return 1 / recursion(base, -power)

            if power % 2 == 0:
                return recursion(base * base, power // 2)
            elif power % 2 != 0:
                return base * recursion(base * base, (power - 1) // 2)

        return recursion(x, n)
