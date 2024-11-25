"""
n = 3, m = 2
(1,2)
  Y Y | X
    A B | A
(3,2)
  Y Y | X X X
(2, 1)
  Y | X X

n = 1, m = 1
  X: [1, 1]
  Y: [1, 1]
  Y | X

Obs
  The number of flowers needs to be odd
  With the range constraints, generates pairs of two numbers whose sum is odd
  Circular thing doesn't matter

Brute force
  T: O(N**2), S: O(N**2)
    10,000,000,000
Ans
  T: <O(N**2), S: <O(N**2)

When is the sum odd?
  either of 2 is odd and the other is even

x: [1, 3]
  odd: 2, even: 1
y: [1, 2]
  odd: 1, even: 1
ans: 3

  x.odd * y.even + x.even * y.odd

x: [1, 1]
y: [1, 5]

if n is odd
  odd: n // 2 + 1
  even: n // 2
if n is even
  odd: n // 2
  even: n // 2
"""


class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        if n % 2 != 0:
            x_odd = n // 2 + 1
            x_even = n // 2
        else:
            x_odd = n // 2
            x_even = n // 2

        if m % 2 != 0:
            y_odd = m // 2 + 1
            y_even = m // 2
        else:
            y_odd = m // 2
            y_even = m // 2

        # print(x_odd, x_even, y_odd, y_even)

        return x_odd * y_even + x_even * y_odd

    def flowerGame2(self, n: int, m: int) -> int:
        ans = 0

        for x in range(1, n + 1):
            for y in range(1, m + 1):
                if (x + y) % 2 != 0:
                    ans += 1

        return ans

    def flowerGame1(self, n: int, m: int) -> int:
        pairs = set()

        for x in range(1, n + 1):
            for y in range(1, m + 1):
                if (x + y) % 2 != 0:
                    pairs.add((x, y))

        # print(pairs)

        return len(pairs)