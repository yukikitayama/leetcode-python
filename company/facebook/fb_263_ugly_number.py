"""
- While loop until 1 by divided by 2, 3, 5
"""


class Solution:
    def isUgly(self, n: int) -> bool:

        for p in [2, 3, 5]:
        # for p in [5, 3, 2]:

            # n > 0 because problem says ugly number needs to be positive
            while n % p == 0 and n > 0:

                n /= p

        return n == 1


if __name__ == '__main__':
    n = 6
    print(Solution().isUgly(n))
