from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_subarray = max_subarray = nums[0]

        for num in nums[1:]:
            # If current num is negative, num > current_subarray + num
            # , and successfully restart with a new num to sum
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)

        return max_subarray


"""
Kadane's algorithm from dynamic programming
Time: O(n), Space: O(1)
"""

