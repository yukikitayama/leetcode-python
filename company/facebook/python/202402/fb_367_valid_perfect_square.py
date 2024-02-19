"""
Try integer from 1 to num and square
  if squared equal to num
    return True
After iteration complete, return False
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        left = 2
        right = num // 2

        while left <= right:

            mid = left + (right - left) // 2

            square = mid * mid

            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1

        return False
