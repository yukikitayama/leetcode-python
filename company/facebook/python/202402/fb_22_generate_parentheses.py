"""
hashmap
  k: "(", ")"
  v: count

backtracking(comb, balance)
  terminate if balance is 0, comb length is n * 2
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        p_to_c = {
            "(": n,
            ")": n
        }

        ans = []

        def backtracking(curr_comb, balance):

            if len(curr_comb) == n * 2 and balance == 0:
                ans.append("".join(curr_comb))
                return

            if balance < 0:
                return

            if len(curr_comb) > n * 2:
                return

            for p in p_to_c:

                if p_to_c[p] > 0:
                    p_to_c[p] -= 1
                    curr_comb.append(p)
                    balance += 1 if p == "(" else -1

                    backtracking(curr_comb, balance)

                    balance -= 1 if p == "(" else -1
                    curr_comb.pop()
                    p_to_c[p] += 1

        backtracking([], 0)

        return ans