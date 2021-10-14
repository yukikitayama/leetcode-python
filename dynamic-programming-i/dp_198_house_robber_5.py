from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_robbed_amount = [0] * (len(nums) + 1)

        max_robbed_amount[len(nums)] = 0
        max_robbed_amount[len(nums) - 1] = nums[-1]

        for i in range(len(nums) - 2, -1, -1):

            max_robbed_amount[i] = max(max_robbed_amount[i + 1], max_robbed_amount[i + 2] + nums[i])

        return max_robbed_amount[0]
