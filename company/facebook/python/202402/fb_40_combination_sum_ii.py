"""
Backtracking(curr_sum)
"""

from typing import List
import collections


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)

        ans = []

        def backtracking(curr_sum, curr_comb, index):

            if curr_sum == target:
                ans.append(curr_comb[:])
                return

            for i in range(index, len(candidates)):

                if index < i and candidates[i] == candidates[i - 1]:
                    continue

                if curr_sum + candidates[i] > target:
                    continue

                else:
                    curr_comb.append(candidates[i])

                    backtracking(curr_sum + candidates[i], curr_comb, i + 1)

                    # Backtracking
                    curr_comb.pop()

        backtracking(0, [], 0)

        return ans

    def combinationSum21(self, candidates: List[int], target: int) -> List[List[int]]:
        counter = collections.Counter(candidates)
        keys = sorted(list(counter.keys()), reverse=True)

        print(keys)

        ans = []

        def backtracking(curr_sum, curr_comb, index):

            if curr_sum == target:
                ans.append(curr_comb[:])
                return

            for i in range(index, len(keys)):

                k = keys[i]

                if curr_sum + k > target:
                    continue

                if counter[k] > 0:
                    curr_comb.append(k)
                    counter[k] -= 1

                    backtracking(curr_sum + k, curr_comb, i)

                    curr_comb.pop()
                    counter[k] += 1

        backtracking(0, [], 0)

        return ans
