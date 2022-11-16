"""
- Binary search
"""

def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:

            mid = (left + right) // 2

            res = guess(mid)

            if res == 0:
                return mid
            elif res == -1:
                right = mid - 1
            else:
                left = mid + 1

