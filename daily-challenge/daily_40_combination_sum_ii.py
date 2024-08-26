from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        ans = []

        def backtracking(index, comb, sum_):

            if sum_ == target:
                ans.append(comb[:])
                return

            for i in range(index, len(candidates)):

                # [1, 1, 1, 2], target: 4, comb: [1, 1 (2nd), 2]
                # When index: 1, [1, 1, _, _] can, [1, _, 1, _] cannot, because already picked the same number
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] + sum_ > target:
                    continue

                comb.append(candidates[i])

                backtracking(i + 1, comb, sum_ + candidates[i])

                comb.pop()

        backtracking(0, [], 0)

        return ans
