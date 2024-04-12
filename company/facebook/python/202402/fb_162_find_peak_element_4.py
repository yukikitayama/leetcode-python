from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Edge
        if len(nums) == 1:
            return 0

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if (
                    (mid == 0 and nums[mid] > nums[mid + 1])
                    or (mid == len(nums) - 1 and nums[mid - 1] < nums[mid])
                    or (nums[mid - 1] < nums[mid] > nums[mid + 1])
            ):
                return mid

            elif nums[mid] > nums[mid + 1]:
                right = mid - 1

            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
