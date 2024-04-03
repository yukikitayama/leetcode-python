class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_digits = 0
        y = x
        while y:
            sum_digits += y % 10
            y //= 10

        if x % sum_digits == 0:
            return sum_digits
        else:
            return -1
