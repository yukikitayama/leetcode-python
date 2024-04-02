"""
Min heap
"""

from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Counting sort"""
        max_num = max(nums)
        min_num = min(nums)
        range_ = max_num - min_num + 1
        counts = [0] * range_

        for i in range(len(nums)):
            num = nums[i] - min_num
            counts[num] += 1

        # print(counts)

        for i in range(len(counts) - 1, -1, -1):
            k -= counts[i]

            if k <= 0:
                return i + min_num

    def findKthLargest1(self, nums: List[int], k: int) -> int:
        """Min heap"""
        min_heap = []

        for i in range(len(nums)):

            heapq.heappush(min_heap, nums[i])

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]
