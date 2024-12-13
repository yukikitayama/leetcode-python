from typing import List
import heapq


class Solution:
    def findScore(self, nums: List[int]) -> int:
        ans = 0

        min_heap = []
        for i, num in enumerate(nums):
            heapq.heappush(min_heap, (num, i))

        marked = [False] * len(nums)
        while min_heap:
            num, i = heapq.heappop(min_heap)

            if not marked[i]:
                ans += num
                marked[i] = True

                if i - 1 >= 0:
                    marked[i - 1] = True
                if i + 1 < len(nums):
                    marked[i + 1] = True

        return ans