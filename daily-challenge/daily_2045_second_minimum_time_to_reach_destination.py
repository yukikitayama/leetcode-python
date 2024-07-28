"""
If the current time falls between 2 * m * c and 2 * m * c + c, where m is any integer, we have a green signal for the node, otherwise, we have a red signal.

Since we need the second minimal distance, each node can be poped out at most twice.
"""

from typing import List
import collections
import heapq


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        time1 = [float("inf")] * n
        time2 = [float("inf")] * n
        freq = [0] * n

        # [(time from city 1, city), ...]
        min_heap = []
        # City is 1-based
        heapq.heappush(min_heap, (0, 1))
        # Array index is 0-based
        time1[0]

        while min_heap:

            curr_time, curr_city = heapq.heappop(min_heap)

            freq[curr_city - 1] += 1

            if freq[curr_city - 1] == 2 and curr_city == n:
                return curr_time

            # curr_time: 2, change: 5, curr_time // change: 0, signal: green
            # curr_time: 7, change: 5, curr_time // change: 1, signal: red
            # curr_time: 12, change: 5, curr_time // change: 2, signal: green
            # If red
            if (curr_time // change) % 2 == 1:
                # change * (curr_time // change + 1) returns the time when red ends
                # so the entire formula returns the time after spending time during green right after red ends
                # time: , curr_time: 6, change: 5, curr_time // change: 1,
                # change * (curr_time // change + 1): 5 * 2 = 10
                # above + time: 10 + 3 = 13
                next_time = change * (curr_time // change + 1) + time

            # If green
            elif (curr_time // change) % 2 == 0:
                next_time = curr_time + time

            for neighbor in adj[curr_city]:

                # ?
                if freq[neighbor - 1] == 2:
                    continue

                # If currently minimum time found
                if next_time < time1[neighbor - 1]:
                    time2[neighbor - 1] = time1[neighbor - 1]
                    time1[neighbor - 1] = next_time
                    heapq.heappush(min_heap, (next_time, neighbor))

                # If currently second minimum time found
                elif next_time < time2[neighbor - 1] and next_time != time1[neighbor - 1]:
                    time2[neighbor - 1] = next_time
                    heapq.heappush(min_heap, (next_time, neighbor))

        return 0
