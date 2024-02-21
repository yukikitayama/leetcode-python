"""
Prefix sum
  from 0
  [0, -2, -2, 1]
    [0, 2] -> prefix_sum[2 + 1] - prefix_sum[0]
    [2, 5] -> prefix_sum[5 + 1] - prefix_sum[2]
"""

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0]
        for i in range(len(nums)):
            self.prefix_sum.append(self.prefix_sum[-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)