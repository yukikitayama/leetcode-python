"""
1199, 99
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        # i = 0
        # carry = 0
        # ans = []

        # # Make equal length
        # if len(num1) < len(num2):
        #     num1 = "0" * (len(num2) - len(num1)) + num1
        # elif len(num1) > len(num2):
        #     num2 = "0" * (len(num1) - len(num2)) + num2

        # for i in range(len(num1)):
        #     n1 = ord(num1[-(i + 1)]) - ord("0")
        #     n2 = ord(num2[-(i + 1)]) - ord("0")

        #     sum_ = n1 + n2 + carry
        #     carry = sum_ // 10
        #     digit = sum_ % 10
        #     ans.append(digit)

        # if carry:
        #     ans.append(carry)

        # ans.reverse()

        # return "".join(str(digit) for digit in ans)

        ans = []
        carry = 0
        p1 = 0
        p2 = 0

        while p1 < len(num1) or p2 < len(num2):
            n1 = ord(num1[-(p1 + 1)]) - ord("0") if p1 < len(num1) else 0
            n2 = ord(num2[-(p2 + 1)]) - ord("0") if p2 < len(num2) else 0
            sum_ = n1 + n2 + carry
            carry = sum_ // 10
            digit = sum_ % 10
            ans.append(digit)
            p1 += 1
            p2 += 1

        if carry:
            ans.append(carry)

        ans.reverse()
        return "".join([str(d) for d in ans])