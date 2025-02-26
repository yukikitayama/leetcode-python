"""
Additionally, since a subarray can start at the very beginning of the array, we also compare the absolute value of the prefix sum itself against our current maximum absolute sum.

The greater the difference between prefixSum[j] and prefixSum[i], the larger the absolute sum of the subarray. Thus, to maximize this difference, prefixSum[j] should be as large as possible, while prefixSum[i] should be as small as possible.

the absolute difference between maxPrefixSum and minPrefixSum gives us the maximum absolute subarray sum
"""

from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_so_far = 0
        max_so_far = 0
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            min_so_far = min(min_so_far, prefix_sum)
            max_so_far = max(max_so_far, prefix_sum)
        return max_so_far - min_so_far

    def maxAbsoluteSum1(self, nums: List[int]) -> int:
        min_so_far = float("inf")
        max_so_far = float("-inf")
        prefix_sum = 0
        # 0 for empty subarray
        ans = 0

        for num in nums:

            prefix_sum += num

            min_so_far = min(min_so_far, prefix_sum)
            max_so_far = max(max_so_far, prefix_sum)

            if prefix_sum >= 0:
                ans = max(
                    ans,
                    max(
                        prefix_sum,
                        prefix_sum - min_so_far
                    )
                )

            else:
                ans = max(
                    ans,
                    max(
                        abs(prefix_sum),
                        abs(prefix_sum - max_so_far)
                    )
                )

        return ans