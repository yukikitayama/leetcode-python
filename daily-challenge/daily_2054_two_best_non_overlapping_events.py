from typing import List
import heapq


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()

        # [(end, value), ...]
        min_heap = []
        ans = 0
        max_val = 0

        for start, end, val in events:
            # If found non-overlapping
            # min_heap[0][0]: end
            while min_heap and min_heap[0][0] < start:
                # min_heap[0][1]: value
                max_val = max(max_val, min_heap[0][1])
                heapq.heappop(min_heap)

            ans = max(
                ans,
                max_val + val
            )

            heapq.heappush(min_heap, (end, val))

        return ans