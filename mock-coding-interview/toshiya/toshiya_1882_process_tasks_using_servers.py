"""
Iterate tasks array
  For each task, find a server which has smallest weight, smallest index, and free
  Heap (Priority queue)
    [(available time, weight, index)]
      [(0, 2, 2), (0, 3, 0), (0, 3, 1)]
"""

from typing import List
import heapq


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:

        ans = []

        # [(weight, index), ...]
        min_heap_available = []
        for i in range(len(servers)):
            heapq.heappush(min_heap_available, (servers[i], i))
        # [(available time, weight, index), ...]
        min_heap_busy = []

        for curr_time, task_time in enumerate(tasks):

            # Check if busy server is available at current time
            while min_heap_busy and min_heap_busy[0][0] <= curr_time:
                # Move the currently available server from busy to available
                available_time, weight, server_index = heapq.heappop(min_heap_busy)
                heapq.heappush(min_heap_available, (weight, server_index))

            # If there are available servers
            if len(min_heap_available) > 0:
                # Get available server
                weight, server_index = heapq.heappop(min_heap_available)

                # Record server
                ans.append(server_index)

                # Mark the available server busy
                heapq.heappush(min_heap_busy, (curr_time + task_time, weight, server_index))

            # If no servers available, we will wait until one of the busy servers is available
            # in code, we will taks a server from busy servers which will be available first
            else:
                # Get the first available server from busy servers
                server_time, weight, server_index = heapq.heappop(min_heap_busy)

                # Record server
                ans.append(server_index)

                # Mark the busy server with updated info
                heapq.heappush(min_heap_busy, (server_time + task_time, weight, server_index))

            # print(f"curr_time: {curr_time}, server: {server_index}, available: {min_heap_available}, buys: {min_heap_busy}")

        return ans
