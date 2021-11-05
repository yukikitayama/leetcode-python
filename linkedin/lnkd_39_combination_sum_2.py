from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtracking(curr, index, remaining):

            # print(f'  in backtracking, curr: {curr}, index: {index}, remaining: {remaining}')

            if remaining < 0:
                return

            if remaining == 0:
                # Need to append the copy of the current array, otherwise it save reference
                # and the values in array change
                ans.append(curr[:])

            for i in range(index, len(candidates)):

                curr_num = candidates[i]
                curr.append(curr_num)

                backtracking(curr, i, remaining - curr_num)

                # Backtracking
                curr.pop()

        backtracking([], 0, target)

        return ans


candidates = [2, 3, 6, 7]
target = 7
candidates = [2,3,5]
target = 8
print(Solution().combinationSum(candidates, target))

