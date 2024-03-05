"""
Valid tree means no cycle
cycle detection algorithm
count indegree of each node
BFS from indegree 1 nodes
  when visit neighbor node, if indegree is 1, it can
Check visited boolean array are all True

Ans
  Tree if graph is fully connected and no cycle
"""

from typing import List
import collections


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        queue = collections.deque()
        queue.append(0)
        visited = set([0])

        while queue:

            for _ in range(len(queue)):
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        return len(visited) == n

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        curr_to_parent = {0: -1}

        # Iterative DFS
        stack = [0]

        while stack:

            curr = stack.pop()

            for neighbor in graph[curr]:

                # Trivial undirected graph cycle so no need to visit
                # {3: 0} when visited from 0 to 3
                if neighbor == curr_to_parent[curr]:
                    continue

                # Visiting the same node previously visited, not trivial cycle of undirected graph, so cycle
                if neighbor in curr_to_parent:
                    return False

                curr_to_parent[neighbor] = curr
                stack.append(neighbor)

        return len(curr_to_parent) == n

    def validTree1(self, n: int, edges: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        indegrees = [0] * n
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            indegrees[edge[0]] += 1
            indegrees[edge[1]] += 1

        print(indegrees)

        visited = [False] * n

        queue = collections.deque()
        for i in range(len(indegrees)):
            if indegrees[i] == 1:
                queue.append(i)

        while queue:

            for _ in range(len(queue)):

                node = queue.popleft()
                visited[node] = True

                for neighbor in graph[node]:
                    indegrees[neighbor] -= 1
                    if indegrees[neighbor] == 1 and not visited[neighbor]:
                        queue.append(neighbor)

        return sum(visited) == n


