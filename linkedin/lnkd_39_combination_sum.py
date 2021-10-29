"""
- backtracking?
  - backtracking stops when the sum is equal to target
    - and the list to answer
  - backtracking also stops when the sum is greater than target
    - but it does not add the current list to answer
- This problem asks combination, not permutation
  - That's why in iterating each candidate in candidates.
    It cannot go back to the previous number, because
    it will make duplicated combinations
"""


from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtracking(remain, combination, start):

            if remain == 0:
                ans.append(combination[:])
                return

            if remain < 0:
                return

            for i in range(start, len(candidates)):
                curr_num = candidates[i]
                combination.append(curr_num)

                backtracking(remain - curr_num, combination, i)

                combination.pop()

        ans = []

        # First arg is the difference between target and current sum
        # initially sum is 0, so pass target itself
        # Second arg is temporary combination
        # Third arg is the index to pick candidate
        backtracking(target, [], 0)

        return ans


candidates = [2,3,6,7]
target = 7
candidates = [2,3,5]
target = 8
candidates = [2]
target = 1
candidates = [1]
target = 1
candidates = [1]
target = 2
print(Solution().combinationSum(candidates, target))
