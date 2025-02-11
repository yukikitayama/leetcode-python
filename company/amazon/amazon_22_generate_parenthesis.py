"""
backtracking(comb, balance)
  terminate
    comb length is n * 2 and balance is 0
  recurrence
    ( or )
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def backtracking(comb, balance):

            # Invalid
            if balance < 0:
                return

            # Valid
            elif (len(comb) == n * 2) and balance == 0:
                ans.append("".join(comb[:]))
                return

                # Invalid
            elif len(comb) == n * 2:
                return

            for next_ in ["(", ")"]:
                comb.append(next_)

                backtracking(comb, balance + 1 if next_ == "(" else balance - 1)

                comb.pop()

        backtracking([], 0)

        return ans
