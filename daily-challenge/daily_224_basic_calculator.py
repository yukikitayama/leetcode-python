class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        n = 0
        operand = 0

        for i in range(len(s) - 1, -1, -1):

            ch = s[i]

            if ch.isdigit():

                operand = (10 ** n * int(ch)) + operand
                n += 1

            elif ch != " ":

                # print(f'before stack: {stack}')

                # Append digit
                if n:
                    stack.append(operand)
                    n = 0
                    operand = 0

                # Compute expression in parenthesis and append the digit
                if ch == '(':
                    res = self.evaluate_expr(stack)

                    # Discard ')'
                    stack.pop()

                    stack.append(res)

                # Append non-digit
                else:
                    stack.append(ch)

                # print(f' after stack: {stack}')

            # Ignore spaces

        # print(f'before stack: {stack}')

        if n:
            stack.append(operand)

        # print(f'after stack: {stack}')

        return self.evaluate_expr(stack)

    def evaluate_expr(self, stack):

        if not stack or type(stack[-1]) == str:
            stack.append(0)

        res = stack.pop()

        while stack and stack[-1] != ')':

            sign = stack.pop()

            if sign == '+':
                res += stack.pop()
            else:
                res -= stack.pop()

        return res


if __name__ == '__main__':
    s = "(1+(4+5+2)-3)+(6+8)"
    print(Solution().calculate(s))
