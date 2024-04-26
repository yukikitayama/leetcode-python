from typing import List
import collections


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1

        item_graph = collections.defaultdict(list)
        item_indegree = [0] * n
        group_graph = collections.defaultdict(list)
        group_indegree = [0] * group_id

        for curr in range(n):
            # beforeItems[curr] is array
            for prev in beforeItems[curr]:

                item_graph[prev].append(curr)
                item_indegree[curr] += 1

                if group[curr] != group[prev]:
                    group_graph[group[prev]].append(group[curr])
                    group_indegree[group[curr]] += 1

        # print(item_graph)
        # print(item_indegree)
        # print(group_graph)
        # print(group_indegree)

        def topological_sort(graph, indegree):

            queue = collections.deque()
            for i in range(len(indegree)):
                if indegree[i] == 0:
                    queue.append(i)

            # Need to be array, not set, because we will use this order
            visited = []

            while queue:

                curr = queue.popleft()

                visited.append(curr)

                for neighbor in graph[curr]:
                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

            if len(visited) == len(indegree):
                return visited
            else:
                return []

        item_order = topological_sort(item_graph, item_indegree)
        group_order = topological_sort(group_graph, group_indegree)

        # print(item_order)
        # print(group_order)

        # No solution due to cycle
        if not item_order or not group_order:
            return []

        # Order items within their groups
        ordered_groups = collections.defaultdict(list)
        for item in item_order:
            ordered_groups[group[item]].append(item)

        # print(ordered_groups)

        ans = []
        for group_index in group_order:
            ans.extend(ordered_groups[group_index])

        return ans
