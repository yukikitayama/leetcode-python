"""
- 9^0 = 1
- 9^1 = 9
- 9^2 = 18

- 10 = 9^1 + 9^0 = 9 + 1 = 0
"""


class Solution:
    def newInteger(self, n: int) -> int:

        ans = ''

        while n:

            # print(f'n: {n}')

            # Find digit from the least significant digit
            # Use % 9 because we wanna skip 9, so
            # 9 % 9 will go back to 0
            # e.g. n: 9, n % 9: 0
            ans = str(n % 9) + ans

            # We wanna decompose number as 9^0 + 9^1 + 9^2 + ...
            # so we remove 9 each time
            # e.g. n: 9, n: 1
            n //= 9

            # print(f'  ans: {ans}')

        return int(ans)


if __name__ == '__main__':
    n = 9
    n = 10
    n = 80  # 88
    n = 81
    # 100
    print(Solution().newInteger(n))
