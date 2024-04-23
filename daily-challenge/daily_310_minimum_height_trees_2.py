"""
bfs from every node
"""

from typing import List
import collections


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # Edge
        if n <= 2:
            return [i for i in range(n)]

        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)

        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []

            while leaves:
                leaf = leaves.pop()
                neighbor = graph[leaf].pop()

                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves

    def findMinHeightTrees1(self, n: int, edges: List[List[int]]) -> List[int]:

        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        heights = [0] * n

        def bfs(node):
            queue = collections.deque([node])
            visited = {node}
            dist = -1
            while queue:
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    for neighbor in graph[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                dist += 1
            return dist

        for i in range(n):
            dist = bfs(i)
            heights[i] = dist

        # print(heights)

        min_value = min(heights)
        ans = []
        for i in range(n):
            if heights[i] == min_value:
                ans.append(i)

        return ans
