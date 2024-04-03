"""
Find leftmost integer, squared < x
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        # Edge
        if x < 2:
            return x

        left = 2
        right = x // 2
        while left <= right:
            mid = (left + right) // 2
            squared = mid * mid

            if squared == x:
                return mid
            elif squared < x:
                left = mid + 1
            elif squared > x:
                right = mid - 1

        return right
