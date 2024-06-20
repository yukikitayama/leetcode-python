"""
Backtracking
Stack
"""

from typing import List


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:

        def math_ops(num1, num2):
            res = [
                num1 + num2,
                num1 - num2,
                num2 - num1,
                num1 * num2,
            ]
            # Avoid 0 division
            if num1 != 0:
                res.append(num2 / num1)
            if num2 != 0:
                res.append(num1 / num2)
            return res

        def backtracking(cards):

            # Base
            if len(cards) == 1:
                return abs(cards[0] - 24) <= 0.1

            # Recurrence relation
            # Pick two numbers from cards
            for i in range(len(cards)):
                for j in range(i + 1, len(cards)):

                    # Remove the 2 numbers from the cards
                    new_cards = [num for k, num in enumerate(cards) if k != i and k != j]

                    # Generate results of all the math operations to the 2 numbers
                    for res in math_ops(cards[i], cards[j]):

                        # Append math operation result to the new array
                        new_cards.append(res)

                        # Recursion with the new array
                        if backtracking(new_cards):
                            return True

                        # Backtrack
                        new_cards.pop()

            return False

        return backtracking(cards)

    def judgePoint241(self, cards: List[int]) -> bool:

        ans = False

        def backtracking(curr_i, curr_res):
            nonlocal ans

            if curr_i == len(cards):
                print(curr_res)
                if curr_res == 24:
                    ans = True
                return

            # +
            backtracking(curr_i + 1, curr_res + cards[curr_i])

            # -
            if curr_i != 0:
                backtracking(curr_i + 1, curr_res - cards[curr_i])

        backtracking(0, 0)

        return ans