from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0

        if len(nums) == 1:
            return nums[0]

        # Because first and last are connected by circle,
        # Do DP to both the array from first to second last and the array from second to last
        # And take the maximum
        return max(self.rob_simple(nums[:-1]), self.rob_simple(nums[1:]))

    def rob_simple(self, nums: List[int]) -> int:
        robbed_max = 0
        prev_1 = 0
        prev_2 = 0

        for current in nums:
            robbed_max = max(current + prev_2, prev_1)
            prev_2 = prev_1
            prev_1 = robbed_max

        return prev_1


"""
Time complexity
Let n be the length of nums. O(n) to iterate for loop

Space complexity
O(1) because there's no dp array
"""


nums = [2,3,2]
nums = [1,2,3,1]
print(Solution().rob(nums))

