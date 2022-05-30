"""
- Use add and subtraction
- dividend / divisor = quotient and remainder
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        MAX_INT = 2147483647  # 2**31 - 1
        MIN_INT = -2147483648  # -2**31
        HALF_MIN_INT = -1073741824  # MIN_INT // 2

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        quotient = 0
        # Both dividend and divisor are turned to be negative
        # So, without sign, dividend needs to be a larger number than divisor
        # with sign, it means that dividend is smaller than divisor
        while dividend <= divisor:

            power_of_two = -1
            value = divisor

            # Double divisor to make things faster
            while value >= HALF_MIN_INT and value + value >= dividend:
                value += value
                power_of_two += power_of_two

            quotient += power_of_two
            # -= because value is negative, and dividend is also negative
            # so -= will remove number from dividend
            dividend -= value

        # If only either dividend or divisor is negative, quotient should be negative
        # we have been treating quotient and negative number
        # If both dividend and divisor are negative (2), quotient will turn out to be positive
        # so multiply -
        return quotient if negatives == 1 else -quotient


if __name__ == '__main__':
    dividend = 10
    divisor = 3
    dividend = 7
    divisor = -3
    print(Solution().divide(dividend, divisor))
