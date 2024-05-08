"""
Total cost
  Sum of edge costs + destination cost + sum of same edge costs * 2

For each city as start
  Apply Dijkstra's algorithm to find min cost
"""

from typing import List
import collections
import heapq


class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:

        graph = collections.defaultdict(list)
        for a, b, cost in roads:
            graph[a - 1].append((b - 1, cost))
            graph[b - 1].append((a - 1, cost))

        def dijkstra(start):
            travel_costs = [float("inf")] * n
            travel_costs[start] = 0
            min_cost = float("inf")
            # [(cumulative cost, city index), ...]
            min_heap = []
            heapq.heapify(min_heap)
            heapq.heappush(min_heap, (0, start))

            while min_heap:

                curr_cost, curr_city = heapq.heappop(min_heap)

                min_cost = min(
                    min_cost,
                    curr_cost + appleCost[curr_city] + k * curr_cost
                )

                for neighbor_city, neighbor_cost in graph[curr_city]:
                    if curr_cost + neighbor_cost < travel_costs[neighbor_city]:
                        travel_costs[neighbor_city] = curr_cost + neighbor_cost
                        heapq.heappush(min_heap, (curr_cost + neighbor_cost, neighbor_city))

            return min_cost

        ans = []

        for start in range(n):
            min_cost = dijkstra(start)
            ans.append(min_cost)

        return ans
