"""
- Make undirected graph from routes
- BFS
  - Queue is a list of (node, depth)
- Two buses are connected if they share at least one bus stop
  - Use set intersection to tell two lists share a common value

"""


from typing import List
import collections
import pprint


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # map(function, iterable), list of sets
        routes = list(map(set, routes))

        # Hashmap with key bus index and value set of bus indices sharing at least one bus stop
        graph = collections.defaultdict(set)
        # i: index to identify one bus
        for i, bus1 in enumerate(routes):
            # j: another index to identify another bus
            for j in range(i + 1, len(routes)):
                bus2 = routes[j]
                # If there's at least one bus stop shared
                if any(stop1 in bus2 for stop1 in bus1):
                    graph[i].add(j)
                    graph[j].add(i)

        # pprint.pprint(graph)

        seen = set()
        targets = set()
        # i: bus index, route: bus stops in the bus index
        # source bus stop and target bus stop might be shared with
        # many buses, so we would gave multiple sources and targets bus index
        for i, route in enumerate(routes):
            if source in route:
                seen.add(i)
            if target in route:
                targets.add(i)

        # BFS
        queue = [(bus_stop, 1) for bus_stop in seen]
        for bus_stop, depth in queue:
            if bus_stop in targets:
                return depth
            for neighbor in graph[bus_stop]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, depth + 1))

        return -1


routes = [[1,2,7],[3,6,7]]
source = 1
target = 6
routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
source = 15
target = 12
print(Solution().numBusesToDestination(routes, source, target))






