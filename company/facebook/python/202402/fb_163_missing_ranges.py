"""
iterate nums
  if next num is not current num + 1, take action
    missing range to create is current num + 1 to next num - 1
  if current num is the last, and if the current num is less than upper
    missing range is current num + 1 to upper

Edge
  nums is empty list
"""

from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        ans = []

        if not nums:
            ans.append([lower, upper])

        for i in range(len(nums)):

            # If first
            if i == 0 and lower < nums[i]:
                end = nums[i] - 1
                ans.append([lower, end])

            # If not first, and not last
            if i < len(nums) - 1:
                if nums[i] + 1 != nums[i + 1]:
                    start = nums[i] + 1
                    end = nums[i + 1] - 1
                    ans.append([start, end])

            # If last
            if i == len(nums) - 1 and nums[i] < upper:
                start = nums[i] + 1
                ans.append([start, upper])

        return ans
