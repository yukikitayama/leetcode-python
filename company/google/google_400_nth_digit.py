"""
n: 3
stream: [1, 2, 3, 4, 5, 6, ...]
Nth digit: 12**3**456

n: 11
stream: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...]
Nth digit: 1234567891**0**11

We have 9 length-1-digits (1, 2, ... 9), 9 - 1 + 1 = 9, +1 because inclusive
90 length-2-digits (10, 11, ..., 99), 99 - 10 + 1 = 90
900 length-3-digits (100, 101, ... 999), 999 - 100 + 1 = 900

https://leetcode.com/problems/nth-digit/discuss/828924/Python3-O(logN)-solution
"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 1
        base = 1

        print(f'n: {n}')

        while n > 9 * digit * base:

            n -= 9 * digit * base
            digit += 1
            base *= 10

        q, r = divmod(n - 1, digit)

        return int(str(base + q)[r])
