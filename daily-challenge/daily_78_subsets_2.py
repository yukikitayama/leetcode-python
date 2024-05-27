from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtracking(index, curr_comb):
            if index == len(nums):
                ans.append(curr_comb[:])
                return

            # Include current number
            curr_comb.append(nums[index])
            backtracking(index + 1, curr_comb)

            # Backtrack
            curr_comb.pop()

            # Skip current number
            backtracking(index + 1, curr_comb)

        backtracking(0, [])

        return ans