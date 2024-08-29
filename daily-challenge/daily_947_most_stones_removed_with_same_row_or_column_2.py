"""
Remove from the stones which have least indegree

Max removable stones = total stones - number of connected components
"""

from typing import List
import collections


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        graph = collections.defaultdict(list)
        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    graph[i].append(j)
                    graph[j].append(i)

        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        num_connected_component = 0

        for i in range(len(stones)):

            if i not in visited:
                dfs(i)
                num_connected_component += 1

        return len(stones) - num_connected_component
