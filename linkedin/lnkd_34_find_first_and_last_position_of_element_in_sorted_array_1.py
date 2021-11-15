"""
- Binary search twice
- Use bisect left and right
"""


from typing import List
import bisect


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return [-1, -1]

        left = bisect.bisect_left(nums, target)

        if left == len(nums) or nums[left] != target:
            left = -1

        right = bisect.bisect_right(nums, target)
        if nums[right - 1] != target:
            right = -1
        else:
            right -= 1

        return [left, right]


nums = [5, 7, 7, 8, 8, 10]
target = 8
nums = [5,7,7,8,8,10]
target = 6
nums = []
target = 0
nums = [2,2]
target = 3
print(Solution().searchRange(nums, target))


