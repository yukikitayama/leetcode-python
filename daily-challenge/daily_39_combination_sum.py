"""
- Backtracking
- Time
  - Let N be the candidates length
  - Let T be the target
  - Let M be the minimal value in candidates
  - Each node can fan out N children
  - Maximal depth is T/M. e.g. Target is 3, minimal is 1, 3/1 = 3, [1, 1, 1]
- Space
  - Recursion stack tree height T/M
  - Temporary store of combination is maximal depth of the tree T/M
"""


from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtracking(curr: List[int], idx: int):

            if sum(curr) == target:
                ans.append(curr[:])

            if sum(curr) > target:
                return

            for i in range(idx, len(candidates)):
                curr.append(candidates[i])

                backtracking(curr, i)

                curr.pop()

        backtracking([], 0)

        return ans


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum(candidates, target))
