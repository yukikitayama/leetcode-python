class Solution:
    def intToRoman(self, num: int) -> str:
        digits = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),
        ]

        roman_digits = []

        for value, symbol in digits:

            if num == 0:
                break

            # If we divide current num with the larger value,
            # quotient will be 0, and the num goes to remainder
            # so it won't add the symbol, because in append(symbol * quotient: 0)
            quotient, remainder = divmod(num, value)

            count = quotient
            num = remainder

            roman_digits.append(symbol * count)

            # print(f'  value: {value}, symbol: {symbol}, '
            #       f'quotient: {quotient}, remainder: {remainder}, '
            #       f'count: {count}')

        return ''.join(roman_digits)


print(Solution().intToRoman(3))
print(Solution().intToRoman(4))
print(Solution().intToRoman(9))
print(Solution().intToRoman(58))
print(Solution().intToRoman(1994))
print(Solution().intToRoman(478))

