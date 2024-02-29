"""
Indegree
Number of edges is n - 1

n: 3, edges: 2
  if one node has only 1 indegree, skip
"""

from typing import List
import collections


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Edge case
        if n <= 2:
            return [i for i in range(n)]

        graph = collections.defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        leaves = collections.deque()
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)

        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)

            new_leaves = collections.deque()

            while leaves:

                leaf = leaves.popleft()

                # Reduce edge
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves

    def findMinHeightTrees1(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        # print(graph)

        def bfs(start):

            queue = collections.deque()
            queue.append(start)
            height = -1
            visited = set()
            visited.add(start)

            while queue:

                for _ in range(len(queue)):

                    curr = queue.popleft()

                    for neighbor in graph[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)

                height += 1

            return height

        node_to_height = collections.defaultdict(int)

        if n == 2:
            return edges[0]

        max_distance_so_far = float("-inf")

        for i in range(n):

            if len(graph[i]) == 1:
                continue
            # BFS
            height = bfs(i)
            node_to_height[i] = height

        # print(node_to_height)

        min_height = min(node_to_height.values())
        ans = []

        for k, v in node_to_height.items():
            if v == min_height:
                ans.append(k)

        return ans
