"""
- DFS?
- Dijkstra's algorithm for single source shortest path
"""


from typing import List
import collections
import heapq


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(list)
        for index, (a, b) in enumerate(edges):
            graph[a].append((b, index))
            graph[b].append((a, index))

        # Why initialize to 0?
        # Because we only use the neighbor when new probability is higher
        p = [0.0] * n
        p[start] = 1.0

        # Max heap: [(current probability, current index), ...]
        heap = [(-p[start], start)]

        while heap:

            curr_prob, curr_index = heapq.heappop(heap)

            if curr_index == end:
                return -curr_prob

            for neighbor, next_index in graph[curr_index]:
                # We use the neighbor only when new probability is bigger
                if -curr_prob * succProb[next_index] > p[neighbor]:
                    p[neighbor] = -curr_prob * succProb[next_index]
                    heapq.heappush(heap, (-p[neighbor], neighbor))

        # Return 0 if no path
        return 0.0


if __name__ == '__main__':
    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    succProb = [0.5, 0.5, 0.2]
    start = 0
    end = 2
    print(Solution().maxProbability(n, edges, succProb, start, end))
