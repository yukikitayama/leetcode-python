"""
Backtracking and hashmap counter
"""

from typing import List
import collections


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = collections.Counter(nums)

        ans = []

        def backtracking(curr_comb):

            if len(curr_comb) == len(nums):
                ans.append(curr_comb[:])
                return

            for k, v in counter.items():
                if v > 0:
                    counter[k] -= 1
                    curr_comb.append(k)

                    backtracking(curr_comb)

                    curr_comb.pop()
                    counter[k] += 1

        backtracking([])

        return ans
