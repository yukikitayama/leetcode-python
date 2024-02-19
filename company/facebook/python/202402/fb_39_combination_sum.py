"""
Backtracking
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []

        def backtracking(index, curr, remaining):

            if remaining == 0:
                ans.append(curr[:])
                return

            if remaining < 0:
                return

            for i in range(index, len(candidates)):
                candidate = candidates[i]

                curr.append(candidate)

                backtracking(i, curr, remaining - candidate)

                curr.pop()

        backtracking(0, [], target)

        return ans
