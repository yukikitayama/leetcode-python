"""
Good pair
  Index diff == value diff
  j - i == nums[j] - nums[i]
  j - nums[j] == i - nums[i]
  Diff between index and value are same for a good pair
  e.g., nums: [1, 1, 2, 1], index: [0, 1, 2, 3],
    index - value: [1, 0, 0, -2]
    i: 1, j: 2 are a good pair
Hashmap
  k: index - value
  v: count
"""

from typing import List
import collections


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        ans = 0
        i_minus_val_to_count = collections.Counter()

        for j in range(len(nums)):
            i_minus_val = j - nums[j]
            num_pairs = j
            num_good_pairs = i_minus_val_to_count[i_minus_val]
            num_bad_pairs = num_pairs - num_good_pairs
            ans += num_bad_pairs

            i_minus_val_to_count[i_minus_val] += 1

        return ans

    def countBadPairs1(self, nums: List[int]) -> int:

        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if j - i != nums[j] - nums[i]:
                    ans += 1

        return ans