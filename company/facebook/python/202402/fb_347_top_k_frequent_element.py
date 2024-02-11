"""
create counter from nums
create heap
  min heap
  if current count is bigger than top, remove top and append current

eg
  1: 3
  2: 2
  3: 1
"""

from typing import List
import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = collections.Counter(nums)

        min_heap = []
        heapq.heapify(min_heap)

        for num, count in counter.items():

            heapq.heappush(min_heap, (count, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for count, num in min_heap]
