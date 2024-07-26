"""
hashmap
  k: city number
  v: hashset of reachable cities
BFS from every city
  continue while each distance is within the distance threshold
"""

from typing import List
import collections
import heapq


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Create adjacency list
        adjacency_list = collections.defaultdict(list)
        for a, b, w in edges:
            adjacency_list[a].append([b, w])
            adjacency_list[b].append([a, w])

        # print(adjacency_list)

        # Initialize shortest path matrix
        shortest_path_matrix = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            shortest_path_matrix[i][i] = 0

        # Define Dijkstra
        def dijkstra(start):
            min_heap = []
            heapq.heappush(min_heap, (0, start))

            while min_heap:
                curr_dist, curr_city = heapq.heappop(min_heap)

                if curr_dist > shortest_path_matrix[start][curr_city]:
                    continue

                for next_city, next_dist in adjacency_list[curr_city]:
                    total_dist = curr_dist + next_dist
                    if total_dist < shortest_path_matrix[start][next_city] and total_dist <= distanceThreshold:
                        shortest_path_matrix[start][next_city] = total_dist
                        heapq.heappush(min_heap, (total_dist, next_city))

        # Start Dijkstra's algorithm from each city
        # Dijkstra updates shortest path matrix
        for i in range(n):
            dijkstra(i)

        # for row in shortest_path_matrix:
        #     print(row)

        # Find a city which has least reachable and highest number
        ans = -1
        min_so_far = n
        for i in range(n):
            count = 0
            for d in shortest_path_matrix[i]:
                if d != 0 and d != float("inf"):
                    count += 1
            # Find a city which is less reachable
            if count < min_so_far:
                ans = i
                min_so_far = count
            # Find a city which has bigger number
            elif count == min_so_far:
                ans = i

            # print(f"i: {i}, count: {count}")

        return ans

    def findTheCity1(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        """MLE"""
        graph = collections.defaultdict(list)
        for from_, to, weight in edges:
            graph[from_].append([to, weight])
            graph[to].append([from_, weight])

        city_to_reachable = collections.defaultdict(set)

        def bfs(start):
            queue = collections.deque()
            queue.append((start, 0))

            while queue:

                for _ in range(len(queue)):

                    curr_city, curr_d = queue.popleft()

                    for neighbor, d in graph[curr_city]:

                        if d + curr_d <= distanceThreshold:
                            if neighbor != start:
                                city_to_reachable[start].add(neighbor)
                            queue.append((neighbor, d + curr_d))

        for i in range(n):
            bfs(i)

        # print(city_to_reachable)

        min_cities = float("inf")
        ans = -1
        for k, v in city_to_reachable.items():
            if len(v) <= min_cities and k > ans:
                ans = k
                min_cities = len(v)
        return ans
