"""
When a < b, a % b is not 0
When a = b, a % b is always 0
When b > a, a % b is 0 if b is divisible by a. eg. 8 / 4 = 2 and no remaining

eg
  [1, 2, 4, 8] share the same factor, 1
  [2, 4, 8] share the same factor, 2

For each number,
  find factors

Hashmap
  k: factor
  v: list of nums which have this factor

Return the longest list
"""

from typing import List
import functools


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        @functools.lru_cache(maxsize=None)
        def dp(i):
            pass

            tail = nums[i]
            ans = []

            for j in range(0, i):

                if tail % nums[j] == 0:
                    subset = dp(j)

                    if len(subset) > len(ans):
                        ans = subset

            ans = ans[:]
            ans.append(tail)

            return ans

        solution = []

        for i in range(len(nums)):
            tmp = dp(i)
            if len(tmp) > len(solution):
                solution = tmp[:]

        return solution