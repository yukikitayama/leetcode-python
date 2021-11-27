from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> int:
        current_position = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= current_position:
                current_position = i

        return current_position == 0


"""
From goal to start one pass
Time: O(n), Space: O(1)
"""

nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
print(Solution().canJump(nums))
