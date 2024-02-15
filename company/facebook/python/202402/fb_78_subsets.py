"""
Backtracking
  append ith element to current set
  recursion
  pop ith element from the set
  and go to the next i
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = [[]]

        def backtracking(i, curr, length):

            if len(curr) == length:
                ans.append(curr[:])
                return

            for j in range(i, len(nums)):
                curr.append(nums[j])

                backtracking(j + 1, curr, length)

                curr.pop()

        for k in range(1, len(nums) + 1):
            backtracking(0, [], k)

        return ans
