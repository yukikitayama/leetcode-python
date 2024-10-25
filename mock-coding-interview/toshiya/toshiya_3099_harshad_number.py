class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_ = 0
        tmp = x
        while tmp > 0:
            # print(tmp % 10, tmp // 10, tmp / 10)
            digit = tmp % 10
            sum_ += digit
            tmp //= 10

        return -1 if x % sum_ != 0 else sum_

    def sumOfTheDigitsOfHarshadNumber1(self, x: int) -> int:
        """T: O(3) = O(1), S: O(3) = O(1)"""
        sum_ = 0
        for digit in str(x):
            sum_ += int(digit)

        if x % sum_ == 0:
            return sum_
        else:
            return -1