"""
[4,5,6,7,0,1,2]

Cut nums into left array and right array
  find which array is sorted
  Check if a target exists in the sorted side
    If yes, continue to search on the sorted side
    If no, search on the other side
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left side is sorted
            elif nums[left] <= nums[mid]:
                # If target might be in left side
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right side is sorted
            elif nums[mid] <= nums[right]:
                # If target might be in right side
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

    def search1(self, nums: List[int], target: int) -> int:

        # Find pivot index
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < nums[-1]:
                right = mid - 1
            elif nums[mid] > nums[-1]:
                left = mid + 1
            # Keep left within nums bound
            elif nums[mid] == nums[-1]:
                right = mid - 1

        # print(left)

        def binary_search(left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            return -1

        # Binary search left of pivot
        res = binary_search(0, left - 1, target)

        if res != -1:
            return res

        # Binary search right of pivot
        res = binary_search(left, len(nums) - 1, target)
        if res != -1:
            return res
        else:
            return -1