from typing import List
import heapq
import math


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)

        ans = 0

        while k:
            curr = heapq.heappop(max_heap)
            curr *= -1

            ans += curr
            k -= 1

            curr = math.ceil(curr / 3)
            heapq.heappush(max_heap, -curr)

        return ans