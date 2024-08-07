class Solution:
    def numberToWords(self, num: int) -> str:

        # Edge case
        if num == 0:
            return "Zero"

        below_ten = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        below_twenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        below_hundred = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        def convert_to_word(num):

            if num < 10:
                return below_ten[num]

            if num < 20:
                # 10 - 10 = 0, below_twenty[10]: "Ten"
                return below_twenty[num - 10]

            if num < 100:
                # num: 20, num // 10: 2, num % 10: 0
                # num: 21, num // 10: 2, num % 10: 1
                # num: 51, num // 10: 5, num % 10: 1
                return below_hundred[num // 10] + (" " + convert_to_word(num % 10) if num % 10 != 0 else "")

            if num < 1000:
                return (
                    convert_to_word(num // 100) + " Hundred" + (
                        " " + convert_to_word(num % 100) if num % 100 != 0 else ""
                    )
                )

            if num < 1000000:
                return (
                    convert_to_word(num // 1000) + " Thousand" + (
                        " " + convert_to_word(num % 1000) if num % 1000 != 0 else ""
                    )
                )

            if num < 1000000000:
                return (
                    convert_to_word(num // 1000000) + " Million" + (
                        " " + convert_to_word(num % 1000000) if num % 1000000 != 0 else ""
                    )
                )

            return (
                convert_to_word(num // 1000000000) + " Billion" + (
                    " " + convert_to_word(num % 1000000000) if num % 1000000000 != 0 else ""
                )
            )

        return convert_to_word(num)