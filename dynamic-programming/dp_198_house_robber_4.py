from typing import List


class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        return self.robFrom(0, nums)

    def robFrom(self, i, nums):
        if i >= len(nums):
            return 0

        if i in self.memo:
            return self.memo[i]

        ans = max(self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i])

        self.memo[i] = ans

        return ans
