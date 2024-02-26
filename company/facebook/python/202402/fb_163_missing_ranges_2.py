"""
Ans array as stack
"""

from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]

        ans = []

        if lower < min(nums):
            ans.append([lower, min(nums) - 1])

        for i in range(1, len(nums)):

            if nums[i] != nums[i - 1] + 1:
                ans.append([nums[i - 1] + 1, nums[i] - 1])

        if upper > max(nums):
            ans.append([max(nums) + 1, upper])

        return ans
