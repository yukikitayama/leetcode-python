from typing import List


class Solution:
    def __init__(self):
        # Total number of arithmetic slices in the given array
        self.sum = 0

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        self.slices(nums, len(nums) - 1)
        return self.sum

    def slices(self, nums: List[int], i: int) -> int:

        # 0 because we are required to have at least 3 elements
        if i < 2:
            return 0

        # ap?
        ap = 0

        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            ap = 1 + self.slices(nums, i - 1)
            self.sum += ap

        else:
            self.slices(nums, i - 1)

        return ap


"""
Top down dynamic programming by using recursive function
"""


nums = [1,2,3,4]
