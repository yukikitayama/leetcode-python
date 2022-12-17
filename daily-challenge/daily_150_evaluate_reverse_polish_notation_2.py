from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # Anonymous function
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
        }

        stack = []
        for token in tokens:
            if token in operations:
                prev = stack.pop()
                prev_prev = stack.pop()
                operation = operations[token]
                result = operation(prev_prev, prev)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack.pop()


class Solution1:
    def evalRPN(self, tokens: List[str]) -> int:

        def evaluate(operator, num1, num2):
            if operator == '+':
                return num1 + num2
            elif operator == '-':
                return num1 - num2
            elif operator == '*':
                return num1 * num2
            elif operator == '/':
                return int(num1 / num2)

        stack = []

        i = 0

        while i < len(tokens):

            curr = tokens[i]

            if curr.isdigit() or (curr[0] == '-' and len(curr) > 1):
                stack.append(int(curr))

            else:
                prev = stack.pop()
                prev_prev = stack.pop()
                result = evaluate(curr, prev_prev, prev)
                stack.append(result)

            i += 1

        return stack.pop()


if __name__ == '__main__':
    # print('11'.isdigit())
    # print('-11'.isdigit())

    tokens = ["2", "1", "+", "3", "*"]
    # 9
    # tokens = ["4", "13", "5", "/", "+"]
    # 6
    # tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    # 22
    print(Solution().evalRPN(tokens))

