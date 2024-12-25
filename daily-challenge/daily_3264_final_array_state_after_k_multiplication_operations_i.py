"""
Min heap [(num, original index), ...]
Create answer array by the indices
"""

from typing import List
import heapq


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        # Operation
        min_heap = []
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i], i))
        while k:
            num, i = heapq.heappop(min_heap)
            num *= multiplier
            heapq.heappush(min_heap, (num, i))
            k -= 1

        # Create answer array
        ans = [0] * len(nums)
        while min_heap:
            num, i = heapq.heappop(min_heap)
            ans[i] = num

        return ans