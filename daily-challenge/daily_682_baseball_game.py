from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for op in ops:

            if op == '+':
                score = stack[-2] + stack[-1]
                stack.append(score)

            elif op == 'D':
                score = stack[-1] * 2
                stack.append(score)

            elif op == 'C':
                stack.pop()

            else:
                stack.append(int(op))

            # print(f'op: {op}, stack: {stack}')

        return sum(stack)


if __name__ == '__main__':
    ops = ["5", "2", "C", "D", "+"]
    ops = ["5","-2","4","C","D","9","+","+"]
    # 27
    print(Solution().calPoints(ops))
