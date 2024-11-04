"""
Greedy
Max heap (Sorting)
  T: NlogN < N^2
"""

from typing import List
import heapq


class Solution:
    def maximumHappinessSum1(self, happiness: List[int], k: int) -> int:

        ans = 0
        happiness.sort(reverse=True)
        reducer = 0
        for i in range(k):
            curr = happiness[i]
            curr -= reducer
            curr = max(0, curr)
            ans += curr
            reducer += 1

        return ans

    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans = 0

        max_heap = []
        for h in happiness:
            heapq.heappush(max_heap, -h)

        reducer = 0

        # while max_heap and k:
        while k:
            # print(max_heap)

            curr = heapq.heappop(max_heap)
            curr *= -1

            curr -= reducer
            curr = max(0, curr)

            ans += curr

            reducer += 1
            k -= 1

        return ans
