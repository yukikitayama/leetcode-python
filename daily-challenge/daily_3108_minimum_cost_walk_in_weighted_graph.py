"""
consider the smallest number in the group. It already has some bits set to 0. Since the AND operation can only turn bits off (changing 1 to 0, but never 0 to 1), the result can never have more 1s than the smallest number. This means the result is always less than or equal to the smallest number.

Therefore, the best way to achieve the lowest cost is to visit every edge in the component.
"""

from typing import List
import collections


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        adj_list = collections.defaultdict(list)
        for a, b, w in edges:
            adj_list[a].append((b, w))
            adj_list[b].append((a, w))

        visited = [False] * n
        # Connected component ID
        component_ids = [0] * n
        component_costs = []

        def get_component_cost(source, component_id):
            queue = collections.deque()
            # -1 & n = n
            component_cost = -1
            queue.append(source)
            visited[source] = True
            while queue:
                node = queue.popleft()
                component_ids[node] = component_id
                for neighbor, weight in adj_list[node]:
                    component_cost &= weight
                    if visited[neighbor]:
                        continue
                    visited[neighbor] = True
                    queue.append(neighbor)
            return component_cost

        component_id = 0
        for node in range(n):
            if not visited[node]:
                cost = get_component_cost(node, component_id)
                component_costs.append(cost)
                component_id += 1

        ans = []
        for start, end in query:
            if component_ids[start] == component_ids[end]:
                ans.append(component_costs[component_ids[start]])
            else:
                ans.append(-1)

        return ans