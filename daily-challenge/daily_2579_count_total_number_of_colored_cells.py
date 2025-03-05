"""
n: 1, ans: 1
n: 2, ans: 5, delta: 4
n: 3, ans: 13, delta: 8
n: 4, ans: 25, delta: 12
n: 5, ans:

For n >= 2
  f: (n - 1) * 4

n: 2, f: 4
n: 3, f: 8,
b: 4, f: 12

Recursion
  if n is 1
    return 1
  if n >= 2
    return recursion(n - 1) + ((n - 1) * 4)

Ans
  we have (n - 1) terms of (n - 1 + 1)
"""


class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 2 * (n - 1) * n

    def coloredCells1(self, n: int) -> int:
        def recursion(n):
            if n == 1:
                return 1

            return recursion(n - 1) + (n - 1) * 4

        return recursion(n)