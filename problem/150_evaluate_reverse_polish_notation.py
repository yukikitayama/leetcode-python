class Solution:
    def evalRPN(self, tokens):
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '/': lambda a, b: int(a / b),
            '*': lambda a, b: a * b
        }
        current_position = 0

        while len(tokens) > 1:
            while tokens[current_position] not in '+-/*':
                current_position += 1

            operator = tokens[current_position]
            number_1 = int(tokens[current_position - 2])
            number_2 = int(tokens[current_position - 1])

            operation = operations[operator]
            # operation() is lambda function
            tokens[current_position] = operation(number_1, number_2)
            # Remove the first two numbers. The number given by the operation gets the first position
            tokens.pop(current_position - 2)
            tokens.pop(current_position - 2)
            current_position -= 1

        return tokens[0]


tokens = ["2","1","+","3","*"]
print(tokens)
sol = Solution()
answer = sol.evalRPN(tokens)
print(f'Answer: {answer}')

# current_position = 2
# tokens[current_position] = "overwritten"
# popped = tokens.pop(current_position - 2)
# print(f'After first pop: {tokens} with popped: {popped}')
# popped = tokens.pop(current_position - 2)
# print(f'After second pop: {tokens} with popped: {popped}')
