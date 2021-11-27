"""

"""


class Solution:
    def calculate(self, s: str) -> str:

        stack = []

        # Initialization for 2 digit or more number
        operand = 0

        res = 0
        # 1 means positive, -1 negative
        sign = 1

        for ch in s:

            print(f'ch: {ch}')

            if ch.isdigit():
                # Scan from left to right, so the current digit can go to the right digit in number
                operand = (operand * 10) + int(ch)

                print(f'In if ch.isdigit(): ch: {ch}, operand: {operand}')

            elif ch == '+':
                res += sign * operand
                sign = 1
                operand = 0

                print(f"In elif ch == '+': res: {res}, sign: {sign}")

            elif ch == '-':
                res += sign * operand
                sign = -1
                operand = 0

                print(f"In elif ch == '-': res: {res}, sign: {sign}")

            elif ch == '(':
                stack.append(res)
                stack.append(sign)

                # Reset operand as if new evaluation begins
                sign = 1
                res = 0

            elif ch == ')':
                res += sign * operand

                # top of the stack is sign
                res *= stack.pop()

                # Next top is operand
                res += stack.pop()

                operand = 0

        print(f'Before return: res: {res}, sign: {sign}, operand: {operand}')

        return res + sign * operand


s = "(1+(4+5+2)-3)+(6+8)"
s = "(1 + (23 + 4))"
s = '1 + (2 + 3)'
s = '-2 + 1'
# s = '123'
print(Solution().calculate(s))
