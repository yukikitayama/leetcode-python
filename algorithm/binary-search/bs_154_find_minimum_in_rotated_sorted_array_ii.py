from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # print(left, mid, right)

            if nums[mid] < nums[right]:
                right = mid

            elif nums[mid] > nums[right]:
                left = mid + 1

            elif nums[mid] == nums[right]:
                right -= 1

        # print(left, mid, right)

        return nums[left]
