"""
x: 4, x/2: 2, ans: 2
x: 9, x/2: 4.5, ans: 3
x: 16, x/2: 8, ans: 4

- square root is always smaller than x/2, and larger than 0

"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = 2
        # // because it could return right, and if x / 2, right is float, not int
        right = x // 2

        while left <= right:

            mid = left + (right - left) // 2

            num = mid * mid

            if num > x:
                right = mid - 1

            elif num < x:
                left = mid + 1

            else:
                return mid

        # When it breaks out of the while loop, left > right.
        # we are required to truncate the decimal digits, so it should return a smaller value,
        # out of while loop, it's right
        return right


"""
Tes
x: 10,
left: 2, right: x // 2 = 5, pivot: 2 + (5 - 2) // 2 = 3, num: 9, num < target, left: pivot + 1 = 4
left: 4, right: 5, pivot: 4 + (5 - 4) // 2 = 4, num: 16, num > target, right: pivot - 1 = 3
left: 4, right: 3, left > right, break while

x: 16,
left: 2, right: x // 2 = 8, pivot: 2 + (8 - 2) // 2 = 5, num: 25, num > target, right: pivot - 1 = 4
left: 2, right: 4, pivot: 2 + (4 - 2) // 2 = 3, num: 9, num < target, left: pivot + 1 = 4
left: 4, right: 4, pivot: 4 + (4 - 4) // 2 = 4, num: 16, return pivot: 4
"""