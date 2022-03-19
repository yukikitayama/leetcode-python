from typing import List


class Solution:
    def __init__(self):
        self.valid_expressions = set()
        self.min_removed = float('inf')

    def backtracking(self, string, index, left_count, right_count, expr, rem_count):
        """
        :param string: Given expression
        :param index: Current index to iterate the given expression
        :param left_count: Number of left opening parentheses
        :param right_count: Number of right closing parentheses
        :param expr: A list of characters currently constructed
        :param rem_count: Number of removals
        :return:
        """

        # If it reached the end of the string
        if index == len(string):

            # If the current expression is valid
            if left_count == right_count:

                # If removal is the minimum number
                if rem_count <= self.min_removed:
                    possible_ans = ''.join(expr)

                    # If the current removals is smaller the previously seen number of removals,
                    # forget about the previous recordings
                    if rem_count < self.min_removed:
                        self.valid_expressions = set()
                        self.min_removed = rem_count

                    self.valid_expressions.add(possible_ans)

        # If the current index is still in the middle of given expression
        else:
            current_char = string[index]

            # If the current character is lower english letter, not parentheses,
            # Just keep going
            if current_char != '(' and current_char != ')':
                expr.append(current_char)
                self.backtracking(string, index + 1, left_count, right_count, expr, rem_count)
                # Backtrack
                expr.pop()

            # If the current character is left-opening or right-closing parenthesis
            else:
                # We have 2 choices; ignore this parenthesis or use this parenthesis

                # Case 1: Ignore current parenthesis, so rem_count + 1
                self.backtracking(string, index + 1, left_count, right_count, expr, rem_count + 1)

                # Case 2: Use current parenthesis
                expr.append(current_char)
                if current_char == '(':
                    self.backtracking(string, index + 1, left_count + 1, right_count, expr, rem_count)

                # If current parenthesis is closing parenthesis,
                # and if number of right-closing parenthesis is smaller than left-opening parenthesis
                # it's potentially still valid, so keep backtracking
                # But otherwise, it won't be valid, so won't backtracking
                elif right_count < left_count:
                    self.backtracking(string, index + 1, left_count, right_count + 1, expr, rem_count)

                # Backtrack
                expr.pop()

    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.backtracking(
            string=s,
            index=0,
            left_count=0,
            right_count=0,
            expr=[],
            rem_count=0
        )

        return list(self.valid_expressions)


if __name__ == '__main__':
    s = "()())()"
    s = "(a)())()"
    print(Solution().removeInvalidParentheses(s))
