"""
k = 3
nums: [1, 2, 0, -1, 4]
  [1, 2]
  [1, 2, 0]
  [0, -1, 4]
  [-1, 4]
prefix sums: [0, 1, 3, 3, 2, 6]
  current prefix sum - previous prefix sum = k
hashmap
  k: prefix sum
  v: count of seen
"""

from typing import List
import collections


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = collections.defaultdict(int)
        prefix_sum = 0
        counter[prefix_sum] += 1
        ans = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum - k in counter:
                ans += counter[prefix_sum - k]

            counter[prefix_sum] += 1

        return ans
