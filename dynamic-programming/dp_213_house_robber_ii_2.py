from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        return max(self.dp(nums[:-1]), self.dp(nums[1:]))

    def dp(self, nums):
        one_back = 0
        two_back = 0
        current = 0

        for i in range(len(nums)):
            current = max(nums[i] + two_back, one_back)
            two_back = one_back
            one_back = current

        return current


"""
"""


nums = [2,3,2]
# nums = [1,2,3,1]
nums = [1,2,3]
print(Solution().rob(nums))

