"""
Hashmap
Heap
  [(3, 1), (2, 2), (1, 3)]
  Min heap
    [(1, 3), (2, 2), (3, 1)]
    keep heap size <= k
    Heap size k -> T: O(NlogK), K < N if there are duplicates

Optimize T: O(N)?
"""

from typing import List
import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = collections.Counter(nums)

        min_heap = []
        heapq.heapify(min_heap)

        for n, v in num_to_count.items():

            heapq.heappush(min_heap, (v, n))

            # print(min_heap, len(min_heap))

            if len(min_heap) > k:
                # print("if")
                heapq.heappop(min_heap)

        return [n for v, n in min_heap]
