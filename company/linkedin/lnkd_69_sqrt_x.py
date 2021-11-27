"""
- Square root si smaller than x / 2
  - e.g. 9: 3^2, 9 / 2 = 4. 5 > 3
  - 16: 4^2, 16 / 2 = 8 > 4
  - 100: 10^2, 100 / 2 = 50 > 10
- Binary search over sorted set of integers
  - Search space is from 2 to x / 2
- Square root of 2 is
  - 1.414...
- Square root of 3
  - 1.732...
- Square root of 4
  - 2
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = 2
        right = x // 2

        while left <= right:
            mid = left + (right - left) // 2
            squared = mid * mid
            if squared > x:
                right = mid - 1
            elif squared < x:
                left = mid + 1
            else:
                return mid
        return right


print(Solution().mySqrt(2))
print(Solution().mySqrt(3))
print(Solution().mySqrt(4))
print(Solution().mySqrt(8))
print(Solution().mySqrt(9))

