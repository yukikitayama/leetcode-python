"""
counter
min heap to keep size k or k + 1
T: O(NlogK)
"""

from typing import List
import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # When k = n, T: O(1), so not O(NlogN)
        if k == len(nums):
            return nums

        # When k < n, T: O(NlogK)
        counter = collections.Counter(nums)

        min_heap = []
        heapq.heapify(min_heap)

        for num, v in counter.items():

            heapq.heappush(min_heap, (v, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [k for v, k in min_heap]
