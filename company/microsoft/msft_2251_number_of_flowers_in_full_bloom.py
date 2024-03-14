"""
Sort flowers
"""

from typing import List
import heapq


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort()
        sorted_people = sorted(people)
        arrival_to_num_flower = {}

        min_heap = []

        # index to flower
        i = 0

        for arrival in sorted_people:

            while i < len(flowers) and flowers[i][0] <= arrival:
                heapq.heappush(min_heap, flowers[i][1])
                i += 1

            # Min end is earlier than arrival, and arrival is also sorted
            # So we won't be able to see this flower any more
            while min_heap and min_heap[0] < arrival:
                heapq.heappop(min_heap)

            arrival_to_num_flower[arrival] = len(min_heap)

        return [arrival_to_num_flower[a] for a in people]
