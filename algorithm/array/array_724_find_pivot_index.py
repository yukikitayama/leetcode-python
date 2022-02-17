from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_ = sum(nums)
        left_sum = 0
        
        for i in range(len(nums)):

            # sum_ - nums[i] - left_sum is right_sum
            if left_sum == sum_ - nums[i] - left_sum:
                return i

            left_sum += nums[i]

        return -1