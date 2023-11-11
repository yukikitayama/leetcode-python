from typing import List
import collections
import heapq


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.adj_list = collections.defaultdict(list)
        for source, destination, cost in edges:
            self.adj_list[source].append((destination, cost))
        self.n = n

    def addEdge(self, edge: List[int]) -> None:
        self.adj_list[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        min_costs = [float("inf") for _ in range(self.n)]

        min_heap = [(0, node1)]
        heapq.heapify(min_heap)
        min_costs[node1] = 0

        while min_heap:

            curr_cost, curr_node = heapq.heappop(min_heap)

            if curr_cost > min_costs[curr_node]:
                continue

            if curr_node == node2:
                return curr_cost

            for nei_node, nei_cost in self.adj_list[curr_node]:
                next_cost = curr_cost + nei_cost

                if next_cost < min_costs[nei_node]:
                    min_costs[nei_node] = next_cost
                    heapq.heappush(min_heap, (next_cost, nei_node))

        return -1



