"""
Backtracking(index, current sum, current combination)
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort(reverse=True)

        ans = []

        def backtracking(index, curr_sum, curr_comb):

            # Termination
            if curr_sum == target:
                ans.append(curr_comb[:])
                return

            if curr_sum > target:
                return

            for i in range(index, len(candidates)):
                curr_comb.append(candidates[i])

                backtracking(i, curr_sum + candidates[i], curr_comb)

                # Backtracking
                curr_comb.pop()

        backtracking(0, 0, [])

        return ans
