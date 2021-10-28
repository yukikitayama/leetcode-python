"""
- by using binary search between 2 and num // 2, make time be O(logn) to search target value
  - the target is mid * mid == num
- space is O(1)
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        left, right = 2, num // 2

        # print(f'left: {left}, right: {right}')

        # num: 2, and num: 3, this while loop is skipped and
        # the last return statement will directly be called
        while left <= right:
            mid = left + (right - left) // 2

            squared = mid * mid

            if squared == num:
                return True

            if squared < num:
                left = mid + 1

            elif squared > num:
                right = mid - 1

        return False


print(Solution().isPerfectSquare(4))
print(Solution().isPerfectSquare(2))
print(Solution().isPerfectSquare(3))
print(Solution().isPerfectSquare(9))
