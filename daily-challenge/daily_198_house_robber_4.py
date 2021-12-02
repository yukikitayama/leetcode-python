"""
- bottom up dp space optimized
"""


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not len(nums):
            return 0

        next_ = nums[-1]
        next_after_next = 0

        for i in range(len(nums) - 2, -1, -1):
            current = max(next_, nums[i] + next_after_next)
            # Shift to right by one
            next_after_next = next_
            next_ = current
        return next_


nums = [1,2,3,1]  # 4
nums = [2,7,9,3,1]  # 12
print(Solution().rob(nums))

