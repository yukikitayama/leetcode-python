"""
Result
- Saw solution: 1
"""


from typing import List
import collections
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # (distance, source vertex)
        heap = [(0, k)]

        dist = {}

        while heap:
            d, node = heapq.heappop(heap)

            # Dijkastra's algorithm is greedy, so if already found the vertex,
            # we already have the min distance.
            if node in dist:
                continue

            dist[node] = d

            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (d + d2, nei))

        # If length of the dictionary is n, it visited all the node
        if len(dist) == n:
            # Max value covers the time all the vertices receiving signal
            ans = max(dist.values())
        # Otherwise, it's impossible for all the vertices to receive the signal
        else:
            ans = -1

        return ans



