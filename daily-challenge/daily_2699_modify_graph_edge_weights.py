from typing import List
import collections
import heapq


class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[
        List[int]]:
        graph = collections.defaultdict(list)
        for a, b, w in edges:
            # Initially ignore -1 weight edge
            if w != -1:
                graph[a].append([b, w])
                graph[b].append([a, w])

        def dijkstra(src, dst):
            min_distance = [float("inf")] * n
            min_distance[src] = 0
            # [(distance, node), ...]
            min_heap = [(0, src)]
            while min_heap:
                distance, node = heapq.heappop(min_heap)

                if distance > min_distance[node]:
                    continue

                for neighbor, weight in graph[node]:
                    if distance + weight < min_distance[neighbor]:
                        min_distance[neighbor] = distance + weight
                        heapq.heappush(min_heap, (min_distance[neighbor], neighbor))

            return min_distance[dst]

        current_shortest_distance = dijkstra(source, destination)

        if current_shortest_distance < target:
            return []

        if current_shortest_distance == target:
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = int(2e9)
            return edges

        for i, (a, b, w) in enumerate(edges):

            if w != -1:
                continue

            edges[i][2] = 1
            # Insert initialized 1
            graph[a].append([b, 1])
            graph[b].append([a, 1])

            new_shortest_distance = dijkstra(source, destination)

            # If found answer
            if new_shortest_distance <= target:
                # If equal, weight 1 will be used
                edges[i][2] += target - new_shortest_distance

                # Remaining egdes are fine with any numbers
                for j in range(i + 1, len(edges)):
                    if edges[j][2] == -1:
                        edges[j][2] = int(2e9)

                return edges

        # return []

    def modifiedGraphEdges1(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[
        List[int]]:

        def dijkstra(source):
            # Initialize distance
            min_distance = [float("inf")] * n
            min_distance[source] = 0

            # Initialize adjacency matrix
            adj_matrix = [[float("inf")] * n for _ in range(n)]
            for a, b, w in edges:
                # Ignore -1 weight edge
                if w != -1:
                    adj_matrix[a][b] = w
                    adj_matrix[b][a] = w

            visited = [False] * n

            # Perform Dijkstra
            for _ in range(n):
                pass

        current_shortest_distance = dijkstra()

        # Even if we assign some positive number to -1, a new path will be longer than current shortest path
        # thus modifying doesn't change the situation
        if current_shortest_distance < target:
            return []
