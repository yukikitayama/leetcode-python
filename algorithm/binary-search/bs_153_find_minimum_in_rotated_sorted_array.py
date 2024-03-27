"""
Find pivot
if current element is bigger than last element
  search to right
if current element is smller than last element
  search to left
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > nums[-1]:
                left = mid + 1
            elif nums[mid] <= nums[-1]:
                right = mid - 1

        # print(left, nums[left])

        return nums[left]
