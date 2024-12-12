from typing import List
import heapq
import math


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Put all the gifts to max heap
        max_heap = []
        for gift in gifts:
            heapq.heappush(max_heap, -gift)

        # While loop k > 0
        while k > 0:

            # Pop top, square root it and push
            gift = -heapq.heappop(max_heap)
            gift = math.floor((gift) ** 0.5)
            heapq.heappush(max_heap, -gift)

            # Decrement k
            k -= 1

        # Return sum of heap
        return -sum(max_heap)