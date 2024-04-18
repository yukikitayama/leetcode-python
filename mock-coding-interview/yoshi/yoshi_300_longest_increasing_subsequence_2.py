"""
1, 2, 3, 4, 8,

5
"""

from typing import List
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = [nums[0]]

        for i in range(1, len(nums)):

            if stack[-1] < nums[i]:
                stack.append(nums[i])

            # Binary search
            else:
                idx = bisect.bisect_left(stack, nums[i])
                stack[idx] = nums[i]

        return len(stack)
