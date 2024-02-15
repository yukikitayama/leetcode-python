"""
Binary search the target
  If curr num isn't target, target doesn't exist
  Position found by the binary search is first position

bisect left to bisect right-1
"""

from typing import List
import bisect


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return [-1, -1]

        left = bisect.bisect_left(nums, target)

        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        right = bisect.bisect_right(nums, target) - 1
        return [left, right]
