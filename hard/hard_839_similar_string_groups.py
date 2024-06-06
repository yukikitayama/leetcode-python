"""
if we can create a path from A to B using words from the group, then A and B are also members of that group.
Each word in strs can be viewed as a node. We add an undirected edge between each pair of similar words. If there is a path in this graph from words A to B, then A and B belong to the same group
"""

from typing import List
import collections


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        def is_similar(i, j):
            diff = 0
            for k in range(len(strs[0])):
                if strs[i][k] != strs[j][k]:
                    diff += 1
            return diff == 0 or diff == 2

        # Create graph from strs
        graph = collections.defaultdict(list)
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if is_similar(i, j):
                    graph[i].append(j)
                    graph[j].append(i)

        # print(graph)

        visited = set()

        def dfs(i):
            visited.add(i)

            for neighbor in graph[i]:
                if neighbor not in visited:
                    dfs(neighbor)

        # DFS to count the number of connected components
        num_connected_component = 0
        for i in range(len(strs)):
            if i not in visited:
                dfs(i)
                num_connected_component += 1

        return num_connected_component
