class Solution:
    def intToRoman(self, num: int) -> str:

        # Use list to keep order from large to small
        int_to_roman = [
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

        ans = []

        for integer, roman in int_to_roman:

            if num == 0:
                break

            count, remainder = divmod(num, integer)

            if count != 0:
                ans.append(roman * count)

            num = remainder

        return ''.join(ans)


if __name__ == '__main__':
    num = 3
    num = 58
    num = 1994
    print(Solution().intToRoman(num))
