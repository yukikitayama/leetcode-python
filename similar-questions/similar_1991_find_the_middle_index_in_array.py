"""
- Similar to 724. Find Pivot Index
"""

from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left_sum = 0
        sum_ = sum(nums)

        for i in range(len(nums)):

            if left_sum == sum_ - nums[i] - left_sum:
                return i

            left_sum += nums[i]

        return -1


if __name__ == '__main__':
    nums = [2, 3, -1, 8, 4]
    print(Solution().findMiddleIndex(nums))
