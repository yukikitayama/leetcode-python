from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)

        # Stop when only one stone is left
        while len(stones) > 1:

            s_1 = heapq.heappop(stones)
            s_2 = heapq.heappop(stones)

            if s_1 != s_2:
                heapq.heappush(stones, -(s_2 - s_1))

        return -heapq.heappop(stones) if stones else 0


