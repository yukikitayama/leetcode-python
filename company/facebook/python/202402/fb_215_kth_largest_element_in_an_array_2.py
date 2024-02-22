"""
min heap of size k
  T: O(NlogK)
when nums length equal to k, min
"""

from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # min_heap = []
        # heapq.heapify(min_heap)

        # for i in range(len(nums)):
        #     heapq.heappush(min_heap, nums[i])
        #     if len(min_heap) > k:
        #         heapq.heappop(min_heap)

        # return min_heap[0]

        min_num = min(nums)
        max_num = max(nums)
        count = [0] * (max_num - min_num + 1)

        for i in range(len(nums)):
            count[nums[i] - min_num] += 1

        # k: 3, count: [2, 2]
        for i in range(len(count) - 1, -1, -1):
            k -= count[i]
            if k <= 0:
                return i + min_num

        return -1