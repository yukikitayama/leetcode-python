"""
DFS
  returns the time to collect the apples in all the subtree
"""

from typing import List
import collections


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def dfs(node, parent):

            total_time = 0

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue

                neighbor_time = dfs(neighbor, node)

                if neighbor_time > 0 or hasApple[neighbor]:
                    total_time += neighbor_time + 2

            return total_time

        return dfs(0, -1)
