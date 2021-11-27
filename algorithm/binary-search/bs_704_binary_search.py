from typing import List


class Solution:
    def search(self, nums: List[int], target: int):
        left = 0
        right = len(nums) - 1

        # <=, not <, to be able to solve len(nums): 1
        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return -1


nums = [-1,0,3,5,9,12]
target = 9
nums = [-1,0,3,5,9,12]
target = 2
nums = [5]
target = 5
print(Solution().search(nums, target))

