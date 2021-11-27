"""
- Reverse Polish Notation is operators follow operands
  - 3 + 4 => 3 4 +
"""


from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for t in tokens:

            if t not in ['+', '-', '*', '/']:
                stack.append(int(t))

            if t == '+':
                curr = stack.pop()
                prev = stack.pop()
                summed = prev + curr
                stack.append(int(summed))

            if t == '-':
                curr = stack.pop()
                prev = stack.pop()
                subtracted = prev - curr
                stack.append(int(subtracted))

            if t == '*':
                curr = stack.pop()
                prev = stack.pop()
                multiplied = prev * curr
                stack.append(int(multiplied))

            if t == '/':
                curr = stack.pop()
                prev = stack.pop()
                divided = prev / curr
                stack.append(int(divided))

        return stack.pop()


class CleanSolution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator_to_lambda = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
        }
        for t in tokens:
            if t in operator_to_lambda:
                curr = stack.pop()
                prev = stack.pop()
                func = operator_to_lambda[t]
                result = func(prev, curr)
                stack.append(result)
            else:
                stack.append(int(t))
        return stack.pop()


# 9
tokens = ["2","1","+","3","*"]
# 6
tokens = ["4","13","5","/","+"]
# 22
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens))

