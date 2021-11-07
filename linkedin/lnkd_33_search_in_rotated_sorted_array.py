"""
- left: 0
- right: len(nums)
- mid = left + (right - left) // 2

- If nums[mid] < target
  - left = mid + 1
- If nums[mid] > target
"""


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # mid and left are in the same increasing subarray
            # e.g. 4(left), 5, 6, 7(mid), 1, 2, 3
            elif nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # mid and left are not in the same increasing subarray
            # 4(left), 5, 6, 1(mid), 2, 3
            elif nums[mid] < nums[left]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1






