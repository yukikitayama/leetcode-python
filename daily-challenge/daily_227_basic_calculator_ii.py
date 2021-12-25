"""
- Stack
"""


class Solution:
    def calculate(self, s: str) -> int:

        if not s:
            return 0

        num = 0
        last_num = 0
        ans = 0
        op = '+'

        for i, char in enumerate(s):

            # print(f'  i: {i}, char: {char}')

            if char.isdigit():
                num = num * 10 + int(char)

            if not char.isdigit() and char != ' ' or i == (len(s) - 1):

                # print(f'    2nd if, op: {op}')

                if op in ['-', '+']:
                    ans += last_num
                    last_num = num if op == '+' else -num
                elif op == '*':
                    last_num = last_num * num
                elif op == '/':
                    last_num = int(last_num / num)

                op = char
                num = 0

        # print(f'stack: {stack}')

        ans += last_num
        return ans


class Solution1:
    def calculate(self, s: str) -> int:

        if not s:
            return 0

        stack = []
        num = 0
        op = '+'

        for i, char in enumerate(s):

            # print(f'  i: {i}, char: {char}')

            if char.isdigit():
                num = num * 10 + int(char)

            if not char.isdigit() and char != ' ' or i == (len(s) - 1):

                # print(f'    2nd if, op: {op}')

                if op == '-':
                    stack.append(-num)
                elif op == '+':
                    stack.append(num)
                elif op == '*':
                    prev_num = stack.pop()
                    result = prev_num * num
                    # print(result)
                    stack.append(result)
                elif op == '/':
                    prev_num = stack.pop()
                    result = int(prev_num / num)
                    # print(result)
                    stack.append(result)

                op = char
                num = 0

        # print(f'stack: {stack}')

        ans = 0
        while stack:
            ans += stack.pop()
        return ans


s = "3+2*2"
s = '14-3/2'
# 13
print(Solution().calculate(s))

