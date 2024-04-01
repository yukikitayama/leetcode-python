"""
DFS
  build graph

From p BFS
  when current value is q
    return distance
"""

from typing import Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        graph = collections.defaultdict(list)

        def dfs(node):
            if node:
                if node.left:
                    graph[node.val].append(node.left.val)
                    graph[node.left.val].append(node.val)
                    dfs(node.left)
                if node.right:
                    graph[node.val].append(node.right.val)
                    graph[node.right.val].append(node.val)
                    dfs(node.right)

        dfs(root)

        # print(graph)

        queue = collections.deque()
        queue.append(p)
        visited = set()
        visited.add(p)
        distance = 0

        while queue:

            for _ in range(len(queue)):

                curr = queue.popleft()

                if curr == q:
                    return distance

                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            distance += 1

