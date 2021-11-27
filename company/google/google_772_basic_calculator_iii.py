class Solution:
    def calculate(self, s: str) -> int:

        print(f's: {s}')

        def update(op, num):
            """
            Do math operation of op to num if op is + or -, and put in stack
            If op is * or /, get the top of the stack and do * or / to the num, and put back in stack
            :param op: operator not yet evaluated
            :param num: current operand
            :return:
            """
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)
            elif op == '*':
                stack.append(stack.pop() * num)
            elif op == '/':
                stack.append(int(stack.pop() / num))

        # Initialization
        stack = []
        num = 0
        op = '+'

        for i in range(len(s)):

            print(f'i: {i}, s[i]: {s[i]}')

            if s[i].isdigit():
                num = num * 10 + int(s[i])

                print(f'num: {num}')

            elif s[i] in ['+', '-', '*', '/', ')']:

                print(f'Running update(op, num) with op: {op} and num: {num}')

                update(op, num)

                if s[i] == ')':
                    num = 0
                    while isinstance(stack[-1], int):
                        num += stack.pop()
                    op = stack.pop()
                    update(op, num)

                num = 0
                op = s[i]

                print(f'op: {op}, num: {num}')

            elif s[i] == '(':
                stack.append(op)
                # Reset
                num = 0
                op = '+'

            print(f'end of each iteration in for loop with: stack: {stack}')
            print()

        print(f'Running update(op, num) with op: {op} and num: {num}')
        update(op, num)
        print(f'Stack before return: stack: {stack}')
        return sum(stack)



# s = "1+1"  # 2
s = "6-4/2"  # 4
# s = "2*(5+5*2)/3+(6/2+8)"  # 21
# s = "(2+6*3+5-(3*14/7+2)*5)+3"  # -12
print(Solution().calculate(s))

