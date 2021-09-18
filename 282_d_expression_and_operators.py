from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        N = len(num)
        answers = []

        # print(f'num: {num}, target: {target}, N: {N}')

        def recurse(index, prev_operand, current_operand, value, string: List[str]):
            # print(f'index: {index}, '
            #       f'prev_operand: {prev_operand}, '
            #       f'current_operand: {current_operand}, '
            #       f'value: {value}, '
            #       f'string: {string}')

            # Done
            if index == N:

                # current_operand == 0?
                # print(f'In if index == N: value: {value}, target: {target}, current_operand: {current_operand}')

                if value == target and current_operand == 0:
                    # [1:] because the first element is always '+' to do "0 +", which we can omit
                    answers.append(''.join(string[1:]))

                    # print(f'Appended an answer to answers')

                # print(f'Recursion done!')

                return

            # At the first iteration
            # current_operand: 0, index: 0
            current_operand = current_operand * 10 + int(num[index])
            str_op = str(current_operand)

            # current_operanc can be 0 if we did +, - or * at the previous iteration
            if current_operand > 0:
                # NO OP recursion
                # At the first iteration
                # prev_operand: 0

                # print(f'Start no op: {value}')

                recurse(index + 1, prev_operand, current_operand, value, string)

                # print('End no op')

            # Addition
            string.append('+')
            string.append(str_op)

            # print(f'Start addition: {value} + {current_operand}')

            recurse(index + 1, current_operand, 0, value + current_operand, string)

            # print('End addition')

            # cancel addition to try other operators
            string.pop()
            string.pop()

            if string:
                # print('In if string')

                # Subtraction
                string.append('-')
                string.append(str_op)

                # print(f'Start subtraction: {value} - {current_operand}')

                recurse(index + 1, -current_operand, 0, value - current_operand, string)
                # Cancel subtraction to try other operators
                string.pop()
                string.pop()

                # Multiplication
                string.append('*')
                string.append(str_op)

                # print(f'Start multiplication: {value} - {prev_operand} + ({current_operand} * {prev_operand})')

                recurse(
                    index + 1,
                    current_operand * prev_operand,
                    0,
                    value - prev_operand + (current_operand * prev_operand),
                    string
                )
                # Cancel multiplication to try other operators
                string.pop()
                string.pop()

        recurse(0, 0, 0, 0, [])
        return answers


num = "123"
target = 6
print(Solution().addOperators(num, target))
