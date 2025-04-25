class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7

        # x is number of digits for a position
        # y is n
        def quickmul(x, y):
            ret = 1
            mul = x
            while y > 0:
                if y % 2 == 1:
                    ret = ret * mul % mod
                mul = mul * mul % mod
                y //= 2

            return ret

        # Formula for total number of good numbers
        return quickmul(5, (n + 1) // 2) * quickmul(4, n // 2) % mod