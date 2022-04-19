"""
- backtracking
- stack

- Divide and conquer

- It's not about where to insert parenthesis,
- But about which part to compute first by dividing and conquer
"""


from typing import List


class Solution:

    def __init__(self):
        self.operation = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b
        }

    def diffWaysToCompute(self, expression: str) -> List[int]:
        # memo: {part of expression: list of computation result}
        # e.g. {'2-1': [1]}

        # print(f'expression: {expression} in diffWaysToCompute')

        return self.evaluate_expression(expression, {})

    def evaluate_expression(self, expression: str, memo: dict) -> List[int]:

        if expression in memo:
            return memo[expression]

        elif expression.isnumeric():
            return [int(expression)]

        results = []

        for i in range(len(expression)):

            # Skip entirely below if the current character is not operator
            if expression[i] not in self.operation:
                continue

            operator = expression[i]

            # print(f'i: {i}, operator: {operator}')

            # Divide
            left_results = self.diffWaysToCompute(expression[:i])
            # +1 because we wanna skip the middle character
            right_results = self.diffWaysToCompute(expression[i + 1:])

            # print(f'left_results: {left_results}, right_results: {right_results}')

            for left in left_results:
                for right in right_results:

                    results.append(self.operation[operator](left, right))

            # print(f'results: {results}, i: {i}')

        memo[expression] = results

        # print(f'memo: {memo}, results: {results}')

        return results


if __name__ == '__main__':
    expression = '2-1-1'
    # expression = '2-1'
    print(Solution().diffWaysToCompute(expression))
