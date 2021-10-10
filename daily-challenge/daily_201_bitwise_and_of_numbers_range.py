"""
7 = 1 * 2^2 + 1 * 2^1 + 1 * 2^0
  = 4 + 2 + 1
  = 7
  = 111
6 = 1 * 2^2 + 1 * 2^1 + 0 * 2^0
  = 4 + 2 + 0
  = 6
  = 110
5 = 1 * 2^2 + 0 * 2^1 + 1 * 2^0
  = 4 + 0 + 1
  = 5
  = 101

    111
    110
    101
AND 100

100 = 1 * 2^2 + 0 * 2^1 + 0 * 2^0
    = 4

9 = 1 * 2^3 + 0 * 2^2 + 0 * 2^1 + 1 * 2^0
  - 1001
10 = 1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 0 * 2^0
  - 1010
11 = 1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 1 * 2^0
   = 8 + 2 + 1
  - 1011
12 = 1 * 2^3 + 1 * 2^2 + 0 * 2^1 + 0 * 2^0
   = 8 + 4 = 12
  - 1101
"""


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0

        # print(f'left: {left}, left bin: {bin(left)} right: {right}, right bin: {bin(right)}, shift: {shift}')

        while left < right:
            # Bit right shift by 1
            left = left >> 1
            right = right >> 1
            shift += 1

            # print(f'  left: {left}, left bin: {bin(left)} right: {right}, right bin: {bin(right)}, shift: {shift}')

        # Get common prefix
        left = left << shift
        return left


left = 5
right = 7
print(Solution().rangeBitwiseAnd(left, right))

