"""
[1, 2, 3]
[01, 10, 11]

01 ^ 10 = 11
11 ^ 10 = 01
"""

from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0

        def backtracking(index, curr_total):
            nonlocal ans

            ans += curr_total

            for i in range(index, len(nums)):
                curr_total ^= nums[i]

                backtracking(i + 1, curr_total)

                # Backtrack
                curr_total ^= nums[i]

        backtracking(0, 0)

        return ans

    def subsetXORSum1(self, nums: List[int]) -> int:

        def compute_xor_total(arr):
            res = 0
            for i in range(len(arr)):
                res ^= arr[i]
            return res

        ans = 0

        def backtracking(index, curr_comb):
            nonlocal ans

            # print(curr_comb)

            ans += compute_xor_total(curr_comb)

            for i in range(index, len(nums)):
                curr_comb.append(nums[i])

                backtracking(i + 1, curr_comb)

                # Backtrack
                curr_comb.pop()

        backtracking(0, [])

        return ans