"""
BFS?
graph
"""

from typing import List
import collections


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target:
            return 0

        graph = collections.defaultdict(list)

        # To save memory, save indices of routes instead of bus stop number
        for route_index, route in enumerate(routes):
            for bus_stop in route:
                graph[bus_stop].append(route_index)

        queue = collections.deque()
        visited_routes = set()

        # Initial routes
        for route_index in graph[source]:
            queue.append(route_index)
            visited_routes.add(route_index)

        ans = 1

        while queue:

            for _ in range(len(queue)):

                curr_route_index = queue.popleft()

                for next_stop in routes[curr_route_index]:

                    if next_stop == target:
                        return ans

                    else:
                        for next_route in graph[next_stop]:
                            if next_route not in visited_routes:
                                queue.append(next_route)
                                visited_routes.add(curr_route_index)
            ans += 1

        return -1


if __name__ == "__main__":
    routes = [[1, 2, 7], [3, 6, 7]]
    source = 1
    target = 6

    routes = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]]
    source = 15
    target = 12

    print(Solution().numBusesToDestination(routes, source, target))
