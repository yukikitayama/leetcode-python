"""
initialize count array with 0 and size k
heap
  [(finish time, server index)]
iterate arrival and load arrays
  keep poping from heap if finish time <= current arrival time
  finish time = arrival + current load
  find which server

"""

from typing import List
import heapq


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        min_heap_free = []
        for i in range(k):
            heapq.heappush(min_heap_free, i)

        # [(end time, server ID), ...]
        #
        min_heap_busy = []

        count = [0] * k

        for i, start in enumerate(arrival):

            # Find servers which become free before or at current start time
            while min_heap_busy and min_heap_busy[0][0] <= start:
                end_time, server_id = heapq.heappop(min_heap_busy)
                # i+ maintains time series
                # (server_id - i) % k maintains (i % k)th server availability
                modified_id = i + (server_id - i) % k
                heapq.heappush(min_heap_free, modified_id)

            if len(min_heap_free) > 0:
                server_id = heapq.heappop(min_heap_free) % k
                heapq.heappush(min_heap_busy, (start + load[i], server_id))
                count[server_id] += 1

        max_count = max(count)
        return [i for i, c in enumerate(count) if c == max_count]