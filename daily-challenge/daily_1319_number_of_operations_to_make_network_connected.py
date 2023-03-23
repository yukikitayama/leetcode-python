from typing import List
import collections


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if len(connections) < n - 1:
            return -1

        adj = collections.defaultdict(list)
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)

        connected_components = 0
        visited = [False] * n

        def dfs(node):
            visited[node] = True

            if node not in adj:
                return

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        for i in range(n):
            if not visited[i]:
                connected_components += 1
                dfs(i)

        return connected_components - 1

