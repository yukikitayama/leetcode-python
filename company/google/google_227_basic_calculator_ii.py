class Solution:
    def calculate(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0

        length = len(s)

        stack = []

        currentNumber = 0
        operation = '+'

        for i in range(length):

            currentChar = s[i]

            # print(f'currentChar: {currentChar}')

            if currentChar.isdigit():
                currentNumber = currentNumber * 10 + int(currentChar)

                # print(f'currentNumber: {currentNumber}')

            if not currentChar.isdigit() and currentChar != ' ' or i == length - 1:
                # +-*/ depends on operation which previous character sets, not the current character.
                if operation == '-':
                    stack.append(-currentNumber)
                elif operation == '+':
                    stack.append(currentNumber)
                elif operation == '*':
                    # print(f"In elif operation == '*'")
                    stack.append(stack.pop() * currentNumber)
                elif operation == '/':
                    # print(f"In elif operation == '/', stack[-1]: {stack[-1]}, currentNumber: {currentNumber}")
                    numerator = stack.pop()
                    # if numerator // currentNumber < 0 and numerator % currentNumber != 0:
                    #     divided = numerator // currentNumber + 1
                    # else:
                    #     divided = numerator // currentNumber
                    divided = int(numerator / currentNumber)
                    stack.append(divided)

                operation = currentChar
                currentNumber = 0

            # print(f'stack: {stack}, operation: {operation}')
            # print()

        result = 0
        while stack:
            result += stack.pop()
        return result


s = '22 - 3 * 5'
s = '14 - 3/2'
s = "10000-1000/10+100*1"
s = '-1000/10'
print(Solution().calculate(s))
