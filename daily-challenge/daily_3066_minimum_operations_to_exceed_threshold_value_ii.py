"""
min heap
pop 2
if heap top is >= k, stop
"""

from typing import List
import heapq


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
        ans = 0

        while len(min_heap) > 1 and min_heap[0] < k:
            x = heapq.heappop(min_heap)
            y = heapq.heappop(min_heap)
            num = min(x, y) * 2 + max(x, y)
            heapq.heappush(min_heap, num)
            ans += 1

        return ans
