"""
two pointers sliding window
hashmap
  k: 0/1
  v: number of the count

cannot expand
  [0, 1, 0, 1, 0, 1, 0]

[0, 1, 0, 0, 0, 0]
"""

from typing import List
import collections


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        count_to_min_index = collections.defaultdict(int)

        count = 0
        count_to_min_index[count] = -1
        ans = 0

        for i in range(len(nums)):

            num = nums[i]

            if num == 1:
                count += 1
            else:
                count -= 1

            if count in count_to_min_index:
                ans = max(ans, i - count_to_min_index[count])
            else:
                count_to_min_index[count] = i

        return ans




