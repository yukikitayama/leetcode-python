"""
BFS and min heap to find shortest paths

Input: n = 6, edges = [[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]]

Output: [true,true,true,false,true,true,true,false]

Explanation:

The following are all the shortest paths between nodes 0 and 5:

The path 0 -> 1 -> 5: The sum of weights is 4 + 1 = 5.
The path 0 -> 2 -> 3 -> 5: The sum of weights is 1 + 1 + 3 = 5.
The path 0 -> 2 -> 3 -> 1 -> 5: The sum of weights is 1 + 1 + 2 + 1 = 5.
"""

from typing import List
import collections
import heapq


class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        graph = collections.defaultdict(list)

        for a, b, w in edges:
            graph[a].append([b, w])
            graph[b].append([a, w])

        def dijkstra(source):
            dist = [float("inf")] * n
            dist[source] = 0
            min_heap = [(0, source)]

            while min_heap:
                curr_weight, curr_node = heapq.heappop(min_heap)

                if dist[curr_node] == curr_weight:

                    for neighbor_node, neighbor_weight in graph[curr_node]:

                        # Update minimum weight
                        if curr_weight + neighbor_weight < dist[neighbor_node]:
                            dist[neighbor_node] = curr_weight + neighbor_weight
                            heapq.heappush(min_heap, (curr_weight + neighbor_weight, neighbor_node))

            return dist

        dist_0 = dijkstra(0)
        dist_n_1 = dijkstra(n - 1)

        # Find shortest path from 0 to each node
        print(dist_0)
        # Find shortest path from n - 1 to each node
        print(dist_n_1)

        # If graph isn't connected
        if dist_0[n - 1] == float("inf"):
            return [False] * len(edges)

        ans = []

        for a, b, w in edges:
            # Check shortest distance with both directions; a to b, b to a

            # a to b
            # dist_0[a] is distance from 0 to a
            # w is distance from a to b
            # dist_n_1[b] is distance from b to n - 1
            path0 = dist_0[a] + w + dist_n_1[b]
            is_shortest_a_b = path0 == dist_0[n - 1]

            # b to a
            # dist_0[b] is distance from 0 to b
            # w is distance from b to a
            # dist_n_1[a] is distance from a to n - 1
            path1 = dist_0[b] + w + dist_n_1[a]
            is_shortest_b_a = path1 == dist_0[n - 1]

            ans.append(is_shortest_a_b or is_shortest_b_a)

        return ans

    def findAnswer1(self, n: int, edges: List[List[int]]) -> List[bool]:
        graph = collections.defaultdict(list)

        for a, b, w in edges:
            graph[a].append([b, w])
            graph[b].append([a, w])

        # [(weight, node)]
        min_heap = []
        heapq.heapify(min_heap)
        heapq.heappush(min_heap, (0, 0))
        distance = 0
        visited = set()
        visited.add(0)

        # while min_heap:

        #     for _ in range(len(min_heap)):

        #         w, node = heapq.heappop(min_heap)

        #         for neighbor_node, neighbor_weight in graph[node]:

        #             if neighbor_node


