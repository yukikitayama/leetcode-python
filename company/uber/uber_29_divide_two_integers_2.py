"""
- Exponential search
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
        # We are working with negative divisor and negative dividend
        # so if divisor >= dividend, e.g. divisor: -5 > dividend: -10
        # If making both positive, divide is bigger than divisor
        # So you should think divide is bigger than divisor here
        while divisor >= dividend:
            power_of_two = -1
            value = divisor

            print(f'  power_of_two: {power_of_two}, value: {value}')

            # Check if double the divisor is too big.
            # If not, keep doubling.
            # value >= HALF_MIN_INT?
            # while value >= HALF_MIN_INT and value + value >= dividend:
            # Both value and dividend are negative,
            # so checking if dividend is bigger than double value
            while value + value >= dividend:
                # Doubling divisor
                value += value
                # Doubling power of two
                power_of_two += power_of_two

                print(f'    value: {value}, power_of_two: {power_of_two}')

            # Update quotient
            quotient += power_of_two

            # Remove value so far so that we can continue with the remainder
            # value is negative, so adding to dividend, but dividend is also negative
            # so dividend is becoming towards 0
            dividend -= value

            print(f'  quotient: {quotient}, power_of_two: {power_of_two}, dividend: {dividend}')
            print()

        return quotient if negatives == 1 else -quotient


dividend = 10
divisor = 3
dividend = 7
divisor = -3
dividend = 694
divisor = 53
print(Solution().divide(dividend, divisor))
