"""
inplace modify and mark -1
"""

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):

            num = abs(nums[i])

            if nums[num - 1] < 0:
                ans.append(num)

            else:
                nums[num - 1] *= -1

        return ans
