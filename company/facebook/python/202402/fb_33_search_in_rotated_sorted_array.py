"""
binary search
  if mid num is target
    return mid
  if mid num > target
    left search space

Ans
  pivot index
    index of smallest element
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        # Find pivot index, left will be pivot index
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            # [1, 2, 3], [4, 1, 2, 3]
            else:
                right = mid - 1

        pivot = left

        def binary_search(left_boundary, right_boundary, target):
            left = left_boundary
            right = right_boundary

            while left <= right:

                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid

                elif nums[mid] > target:
                    right = mid - 1

                else:
                    left = mid + 1

            return -1

        # left half
        left_result = binary_search(0, pivot - 1, target)
        if left_result != -1:
            return left_result

        # Right half
        right_result = binary_search(pivot, n - 1, target)
        return right_result