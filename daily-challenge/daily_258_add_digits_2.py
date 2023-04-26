class Solution:
    def addDigits(self, num: int) -> int:

        ans = 0

        while num:
            ans += num % 10
            num //= 10

            if num == 0 and ans > 9:
                num = ans
                ans = 0

        return ans
