"""
max heap
"""

from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def compute_distance(x, y):
            return x ** 2 + y ** 2

        max_heap = []
        heapq.heapify(max_heap)

        for i in range(len(points)):
            x, y = points[i]

            distance = compute_distance(x, y)

            heapq.heappush(max_heap, (-distance, x, y))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [[x, y] for d, x, y in max_heap]
