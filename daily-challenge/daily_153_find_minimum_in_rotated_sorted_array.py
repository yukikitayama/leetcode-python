from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        # Already sorted case
        if nums[right] > nums[0]:
            return nums[0]

        while right >= left:

            mid = left + (right - left) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                left = mid + 1

            else:
                right = mid - 1


nums = [3,4,5,1,2]
nums = [4,5,6,7,0,1,2]
nums = [11,13,15,17]
print(Solution().findMin(nums))
