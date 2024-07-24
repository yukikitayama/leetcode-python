"""
e.g.
  1: 2
  2: 2
  3: 2

Union Find

[[0,1],[2,3]]

0-1-2-3

Valid tree
- No separation
- No cycle
"""

from typing import List
import collections


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Edge case
        if n == 1:
            return True

        # Edge case
        if len(edges) < n - 1:
            return False

        graph = collections.defaultdict(list)
        indegree = [0] * n
        for a, b in edges:
            indegree[a] += 1
            indegree[b] += 1
            # X{a: b}, O{a: [b, c]}
            graph[a].append(b)
            graph[b].append(a)

        # print(indegree)
        # print(graph)

        queue = collections.deque()
        visited = [False] * n

        for i in range(len(indegree)):
            if indegree[i] == 1:
                queue.append(i)
                visited[i] = True

        while queue:

            for _ in range(len(queue)):

                curr = queue.popleft()

                for neighbor in graph[curr]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 1 and not visited[neighbor]:
                        queue.append(neighbor)
                        visited[neighbor] = True

        return sum(visited) == n