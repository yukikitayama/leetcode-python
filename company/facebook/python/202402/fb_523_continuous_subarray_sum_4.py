"""
k: 6
[23, 2, 4, 6, 7]

[0, 23, 25, 29, 35, 42]
23 % 6 = 5
29 % 6 = 5
3 - 1 = 2

35 % 6 = 5

Hashmap
  k: remainder
  v: first index to see it
"""

from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_to_index = {0: -1}
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            remainder = prefix_sum % k

            if remainder in remainder_to_index:
                prev_i = remainder_to_index[remainder]
                if i - prev_i > 1:
                    return True

            elif remainder not in remainder_to_index:
                remainder_to_index[remainder] = i

        return False