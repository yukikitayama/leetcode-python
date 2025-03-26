"""
median, average

if it is possible to make all elements equal, the optimal final value must be one of the original numbers in the grid, as any other value may require unnecessary extra steps.

a%x=b%x=v%x

This tells us that all numbers in the grid must have the same remainder when divided by x. Otherwise, it is impossible to transform them into a single value using only x-sized steps

our first step is to check if all numbers in the grid have the same remainder when divided by x. If they don't, we immediately return -1. Otherwise, our goal is to find the smallest number of operations required.
"""

from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        ans = 0

        nums = []
        for row in grid:
            for num in row:
                nums.append(num)

        nums.sort()
        # n: 2, median: 1
        # n: 3, median: 1
        median = nums[len(nums) // 2]

        for num in nums:
            if num % x != median % x:
                return -1
            ans += abs(median - num) // x

        return ans
