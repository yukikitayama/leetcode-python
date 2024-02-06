"""
loop
  multiple x many times

When n is negative
  1/x and multiple 1/2 many times

When n = 0
  return 1

T: O(N)
S: T(1)
"""


class Solution:
    # def myPow(self, x: float, n: int) -> float:

    #     if n == 0:
    #         return 1
    #     if n > 0:
    #         ans = 1
    #         for _ in range(n):
    #             ans *= x
    #         return ans
    #     if n < 0:
    #         ans = 1
    #         for _ in range(-n):
    #             ans *= (1 / x)
    #         return ans

    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1

        if n < 0:
            return 1 / self.myPow(x, -n)

        if n % 2 == 0:
            return self.myPow(x * x, n / 2)
        else:
            return x * self.myPow(x * x, (n - 1) / 2)