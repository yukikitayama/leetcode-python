"""
stack to stora numbers
when current token is operator, pop top 2 elements and apply
  save the result to stack

after iterating tokens pop the stack as answer
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        stack = []

        for i in range(len(tokens)):

            if tokens[i] not in operators:

                token = int(tokens[i])
                stack.append(token)

            else:
                operator = tokens[i]
                b = stack.pop()
                a = stack.pop()

                res = operators[operator](a, b)
                stack.append(res)

        return stack[-1]


if __name__ == "__main__":
    tokens = ["2", "1", "+", "3", "*"]  # 9
    tokens = ["4", "13", "5", "/", "+"]  # 6
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]  # 22
    print(Solution().evalRPN(tokens))

