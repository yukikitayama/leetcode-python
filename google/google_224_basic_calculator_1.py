"""
This solution gives us the following error with the input, s = '-2 + 1'
    res -= stack.pop()
TypeError: unsupported operand type(s) for -=: 'str' and 'str'

"""


class Solution:
    def calculate(self, s: str) -> str:

        print(f's: {s}')

        stack = []

        # Initial values to allow a number to start from 1st digit
        # operand is number to be used by operators
        n = 0
        operand = 0

        # -1s to reverse order iterate character in s
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]

            print(f'ch: {ch}')

            if ch.isdigit():

                # current digit is appended to the previous digit from the left
                # so even if it read s in reverse order, number itself is not reversed
                # e.g. '23' is read first 3, and 2, but the below makes it 23, not 32.
                operand = (10 ** n * int(ch)) + operand
                n += 1

                print(f'in if ch.isdigit(): operand: {operand}, n: {n}')

            elif ch != ' ':
                if n:
                    # Put operand first to stack before putting the current operator to stack
                    stack.append(operand)
                    # Reset for the next number
                    n = 0
                    operand = 0

                    print(f'in if n: stack: {stack}')

                # By looking in the reverse order, seeing the '(' is the time to do inner parenthesis operation
                if ch == '(':
                    res = self.evaluate_expr(stack)
                    # This pops ')'. Okay because we don't need to use it for any calculation
                    stack.pop()

                    # Put back in the stack to further calculation
                    stack.append(res)

                # Other non-digits such as '+' and '-' push onto the stack
                else:
                    stack.append(ch)

            print(f'stack: {stack}')

        # Push the last operand
        # This if n is True, for example s: '1 + (2 + 3)'
        # 1 was seen in the if ch.isdigit() but because it was in making operand, but it has not yet been
        # pushed to stack, and the previous digit is still in the stack
        # so to do calculation, push this last digit to stack, and run evaluate_expr() again
        if n:
            stack.append(operand)

            print(f'in the last if n: stack: {stack}')

        # Evaluate anything remaining in stack
        return self.evaluate_expr(stack)

    def evaluate_expr(self, stack):

        res = stack.pop() if stack else 0

        # Evaluate until we get ')'. evaluate_expr() starts with '('
        while stack and stack[-1] != ')':
            sign = stack.pop()
            if sign == '+':
                res += stack.pop()
            else:
                res -= stack.pop()

        return res


class SolutionLC:

    def evaluate_expr(self, stack):

        res = stack.pop() if stack else 0

        # Evaluate the expression till we get corresponding ')'
        while stack and stack[-1] != ')':
            sign = stack.pop()
            if sign == '+':
                res += stack.pop()
            else:
                res -= stack.pop()
        return res

    def calculate(self, s: str) -> int:

        stack = []
        n, operand = 0, 0

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]

            if ch.isdigit():

                # Forming the operand - in reverse order.
                operand = (10**n * int(ch)) + operand
                n += 1

            elif ch != " ":
                if n:
                    # Save the operand on the stack
                    # As we encounter some non-digit.
                    stack.append(operand)
                    n, operand = 0, 0

                if ch == '(':
                    res = self.evaluate_expr(stack)
                    stack.pop()

                    # Append the evaluated result to the stack.
                    # This result could be of a sub-expression within the parenthesis.
                    stack.append(res)

                # For other non-digits just push onto the stack.
                else:
                    stack.append(ch)

        # Push the last operand to stack, if any.
        if n:
            stack.append(operand)

        # Evaluate any left overs in the stack.
        return self.evaluate_expr(stack)


s = "(1+(4+5+2)-3)+(6+8)"
s = "(1 + (23 + 4))"
s = '1 + (2 + 3)'
s = '-2 + 1'
print(Solution().calculate(s))
# print(SolutionLC().calculate(s))
