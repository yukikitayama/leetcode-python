from typing import List
import bisect


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)


nums = [1,3,5,6]
target = 5
nums = [1,3,5,6]
target = 2
nums = [1,3,5,6]
target = 7
nums = [1,3,5,6]
target = 0
nums = [1]
target = 0
print(Solution().searchInsert(nums, target))