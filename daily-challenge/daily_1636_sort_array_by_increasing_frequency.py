"""
Hashmap
  k: num
  v: count
{1: 1, 2: 2, 3: 2}
T: O(NlogN)
S: O(N)

Counting sort
  [0, 1, 2, 3]
  [0, 1, 2, 2]
"""

from typing import List
import collections


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        nums.sort(key=lambda x: (counter[x], -x))
        return nums
