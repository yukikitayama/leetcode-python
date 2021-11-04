"""
- n: 100
  - 4 serves
  - 0.71875

- 0.25 * ((a: 0, b: 100) + (a: 25, b: 75) + (a: 50, b: 50) + (a: 75, b: 25))
  - (a: 0, b: 100)
    = 1
  - (a: 25, b: 75)
    - 0.25 * ((a: 0, b: 75) + (a: 0, b: 50) + (a: 0, b: 25) + (a: 0, b: 0))
      = 0.25 * (1 + 1 + 1 + 0.5) = 0.25 * 3.5 = 0.875
  - (a: 50, b: 50)
    - 0.25 * ((a: 0, b: 50) + (a: 0, b: 25) + (a: 0, b: 0) + (a: 25, b: 0))
      = 0.25 * (1 + 1 + 0.5 + 0) = 0.25 * 2.5 = 0.625
  - (a: 75, b: 25)
    - 0.25 * ((a: 0, b: 25) + (a: 0, b: 0) + (a: 25, b: 0) + (a: 50, b: 0)
      = 0.25 * (1 + 0.5 + 0 + 0) = 0.25 * 1.5 = 0.375
- 0.25 * (1 + 0.875 + 0.625 + 0.375) = 0.25 * 2.875 = 0.71875
"""


import math


class Solution:
    def __init__(self):
        self.memo = {}

    def soupServings(self, n: int) -> float:

        if n >= 4800:
            return 1

        # 25ml = 1 serve
        # e.g. ceil(33.7): 34
        n = math.ceil(n / 25)

        # a, b are remaining serves
        def f(a, b):

            if (a, b) in self.memo:
                return self.memo[(a, b)]

            if a <= 0 and b <= 0:
                return 0.5

            if a <= 0:
                return 1

            # When only soup B is used up, it returns 0 because the probability that we want is
            # the probability that soup A empty first plus A and B empty at the same time.
            if b <= 0:
                return 0

            # 4 operations with equal probability, so 0.25*
            self.memo[(a, b)] = 0.25 * (f(a - 4, b) + f(a - 3, b - 1) + f(a - 2, b - 2) + f(a - 1, b - 3))
            return self.memo[(a, b)]

        return f(n, n)


print(Solution().soupServings(50))
print(Solution().soupServings(100))
print(Solution().soupServings(200))
print(Solution().soupServings(400))
print(Solution().soupServings(800))
print(Solution().soupServings(1600))
print(Solution().soupServings(3200))
print(Solution().soupServings(4800))
print(Solution().soupServings(6400))
