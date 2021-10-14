from typing import List


class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]) -> int:

        self.memo = {}
        return self.robFrom(0, nums)

    def robFrom(self, i, nums):
        # No more houses left to examine at the right side of the array
        # So robber can get no money
        if i >= len(nums):
            return 0

        if i in self.memo:
            return self.memo[i]

        ans = max(self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i])
        self.memo[i] = max(self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i])

        # self.memo[i] = ans
        # return ans
        return self.memo[i]


"""
Recursion and memoization

Time complexity
Let n be the length of nums. O(n) because for loop to each index in nums

Space complexity
O(n) for memoization map and O(n) for recursion stack, so O(n)

This recursion approach might will run into trouble when recursion stack grows too large.
"""


nums = [1, 2, 3, 1]
# nums = [2,7,9,3,1]
print(Solution().rob(nums))

