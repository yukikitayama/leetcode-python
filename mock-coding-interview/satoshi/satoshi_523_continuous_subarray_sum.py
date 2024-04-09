"""
[23,2,4,6,7]
Prefix sum
[0, 23, 25, 29, 35, 42]
Hashmap
  k: prefix sum
  v: index
iterate prefix sum array
  current prefix sum: 29
  29 - 23 = 6
    29's index: 2
    23's index: 0
      current index - prev index = 2

T: O(N^2)

23 % 6 = 5
29 % 6 = 5

If remainers are the same, the sum between these must be 6 (k)
"""

from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_to_idx = {0: -1}
        prefix_sum = 0

        for i in range(len(nums)):

            prefix_sum += nums[i]

            if prefix_sum % k in prefix_to_idx:
                if i - prefix_to_idx[prefix_sum % k] >= 2:
                    return True

            if prefix_sum % k not in prefix_to_idx:
                prefix_to_idx[prefix_sum % k] = i

        return False

    def checkSubarraySum1(self, nums: List[int], k: int) -> bool:
        prefix_to_idx = {0: -1}
        prefix_sum = 0

        for i in range(len(nums)):

            prefix_sum += nums[i]

            for sum_, prev_i in prefix_to_idx.items():
                # print(prefix_sum, sum_)
                if (
                        (prefix_sum - sum_) % k == 0 and i - prev_i >= 2
                        or (prefix_sum - sum_) == 0 and i - prev_i >= 2
                ):
                    return True

            if prefix_sum not in prefix_to_idx:
                prefix_to_idx[prefix_sum] = i

        return False
