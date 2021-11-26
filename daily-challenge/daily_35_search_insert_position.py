"""
- Start: 9:05
- End: 9:12
- Solved: 1
- Saw solution: 0
- Optimized: 1
"""


from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return left


nums = [1,3,5,6]
target = 5
nums = [1,3,5,6]
target = 2
"""
left: 0, right: 3, mid: 0 + (3 - 0) // 2 = 1, nums[1]: 3, else: T, right: 0,
left: 0, right: 0, while: T, mid: 0 + (0 - 0) // 2 = 0, nums[0]: 1, elif: T, left: 0 + 1 = 1,
left: 1, right: 0, while: F
"""
# nums = [1,3,5,6]
# target = 7
print(Solution().searchInsert(nums, target))
