def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2

            result = guess(mid)

            if result == 0:
                return mid
            elif result == -1:
                right = mid - 1
            elif result == 1:
                left = mid + 1

        return -1
