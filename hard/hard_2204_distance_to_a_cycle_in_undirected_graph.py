from typing import List
import collections


class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        indegree = [0] * n

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            indegree[edge[0]] += 1
            indegree[edge[1]] += 1

        # print(graph)
        # print(indegree)

        # Topological sorting to find nodes which belong to cycle
        queue = collections.deque()
        for i in range(n):
            # In bidirectional graph, start node has indegree 1, not 0
            if indegree[i] == 1:
                queue.append(i)

        # Nodes eventuall contains nodes which have indegree more than 1
        # so they belong to cycle
        nodes = set(list(range(n)))
        while queue:
            node = queue.popleft()
            indegree[node] -= 1
            nodes.remove(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 1:
                    queue.append(neighbor)

        # print(nodes)

        ans = [-1] * n
        distance = 0
        queue = collections.deque(list(nodes))
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                # Skip visited node
                if ans[node] != -1:
                    continue

                ans[node] = distance

                for neighbor in graph[node]:
                    # Limit visiting node where we haven't visited
                    if ans[neighbor] == -1:
                        queue.append(neighbor)

            distance += 1

        return ans