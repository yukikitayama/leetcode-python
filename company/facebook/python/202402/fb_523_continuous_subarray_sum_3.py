"""
Prefix sum difference is multiple of k
k: 6
    [23, 2, 4, 6, 7]
[0, 23, 25, 29, 35, 42]
29 - 23 = 6,
3 - 1 = 2 > 1

35 - 29 = 6, but 4 - 3 = 1, not at least two

nested for loop

Hashmap and make T: O(N)
  k: prefix sum
  v: first index to see the prefix sum
If current prefix sum - k is in hashmap
  if current index > first index + 1
"""

from typing import List
import collections


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_to_index = collections.defaultdict(int)

        # eg. nums: [23, 2, 4, 6, 6], k: 7
        # sum([23, 2, 4, 6]): 35, 35 % 7: 0
        # We need to see remainder of 0 before the first occurrence within nums
        remainder_to_index[0] = -1

        prefix_sum = 0

        for i in range(len(nums)):

            prefix_sum += nums[i]
            remainder = prefix_sum % k

            if remainder in remainder_to_index:
                if i > remainder_to_index[remainder] + 1:
                    return True

            else:
                remainder_to_index[remainder] = i

        print(remainder_to_index)

        return False
