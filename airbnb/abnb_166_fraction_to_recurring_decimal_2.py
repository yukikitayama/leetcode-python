class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        quotient, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator * denominator < 0 else ''

        result = [sign + str(quotient), '.']

        remainders = []
        while remainder not in remainders:
            remainders.append(remainder)
            quotient, remainder = divmod(remainder * 10, abs(denominator))
            result.append(str(quotient))

        first_repeat = remainders.index(remainder)

        result.insert(first_repeat + 2, '(')
        result.append(')')
        result = ''.join(result).replace('(0)', '').rstrip('.')
        return result


numerator = 1
denominator = 2
# "0.5"
# numerator = 4
# denominator = 333
# 0.(012)
# numerator = 2
# denominator = 1
# numerator = 2
# denominator = 3
# numerator = 1
# denominator = 5
print(Solution().fractionToDecimal(numerator, denominator))

