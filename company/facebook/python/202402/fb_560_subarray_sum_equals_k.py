"""
If cumulative sum up to i and j has difference of k
  sum of elements between i and j is k

when curr cumsum - prev cumsum = k
  subarray between curr index and prev index has sum k
  curr cumsum - k = prev cumsum
"""

from typing import List
import collections


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0

        cumsum_to_count = collections.defaultdict(int)

        # Empty subarray
        cumsum = 0
        cumsum_to_count[cumsum] = 1

        for i in range(len(nums)):
            cumsum += nums[i]

            if cumsum - k in cumsum_to_count.keys():
                ans += cumsum_to_count[cumsum - k]

            cumsum_to_count[cumsum] += 1

        return ans
