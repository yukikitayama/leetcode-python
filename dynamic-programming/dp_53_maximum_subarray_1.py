from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = float('-inf')

        for i in range(len(nums)):

            current_subarray_sum = 0

            for j in range(i, len(nums)):

                current_subarray_sum += nums[j]

                answer = max(answer, current_subarray_sum)

        return answer


"""
Brute force, TLE, Time: O(n^2), Space: O(1)
"""

