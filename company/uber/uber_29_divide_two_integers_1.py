"""
- Instead of a = a * -1, use a = -a
- Instead of a / 2, use right shift operator, a >> 1
- Instead of a * 2, use right shift operator, a << 1
"""
print(2**31-1)
a = 1
a = -a
print(a)


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647  # 2**31 - 1
        MIN_INT = -2147483648  # -2**31

        # Edge case for max int overflow
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negatives = 2
        if dividend > 0:
            negatives -= 1
            # Make it negative without using *
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        # Count how many times the divisor has to be added
        quotient = 0
        # divisor is negative, so it's adding towards 0
        while dividend - divisor <= 0:
            dividend -= divisor
            quotient -= 1

        # 60 / 10 = 6
        # -60 / 10 = -6
        # 60 / -10 = -6
        # -60 / -10 = 6
        # If originally there's one negative sign, quotient is negative,
        # otherwise switch it to positive
        return quotient if negatives == 1 else -quotient


dividend = 10
divisor = 3
dividend = 7
divisor = -3
print(Solution().divide(dividend, divisor))
