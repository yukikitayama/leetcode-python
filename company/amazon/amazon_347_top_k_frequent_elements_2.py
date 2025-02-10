"""
Hashmap, min heap
"""

from typing import List
import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        min_heap = []
        for num, c in counter.items():
            heapq.heappush(min_heap, (c, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [k for v, k in min_heap]
