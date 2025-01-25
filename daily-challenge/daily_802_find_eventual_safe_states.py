"""
Create graph
Identify terminal node
  count outdegree for each node,
    if 0, terminal node
BFS from terminal node
  collect safe nodes
Sort

Ans
  A node is a safe node if all of its incoming edges come from previously identified safe nodes in the graph.
"""

from typing import List
import collections


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        indegree = [0] * len(graph)
        adj = collections.defaultdict(list)
        for i in range(len(graph)):
            for node in graph[i]:
                adj[node].append(i)
                indegree[i] += 1

        queue = collections.deque()
        for i in range(len(graph)):
            if indegree[i] == 0:
                queue.append(i)

        safe = [False] * len(graph)
        while queue:
            node = queue.popleft()
            safe[node] = True

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        ans = []
        for i in range(len(graph)):
            if safe[i]:
                ans.append(i)

        return ans