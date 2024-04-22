from typing import List
import collections


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ans = False
        visited = set()

        def dfs(node):
            nonlocal ans
            visited.add(node)

            if node == destination:
                ans = True
                return

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(source)

        return ans