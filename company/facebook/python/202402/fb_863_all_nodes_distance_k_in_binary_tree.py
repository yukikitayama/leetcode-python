"""
Tree to graph
BFS from target by k steps
"""

from typing import List
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)

        def dfs(node):
            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                if left:
                    graph[node.val].append(left)
                    graph[left].append(node.val)
                if right:
                    graph[node.val].append(right)
                    graph[right].append(node.val)
                return node.val
            else:
                return None

        dfs(root)

        # print(graph)

        ans = []

        queue = collections.deque()
        queue.append(target.val)
        steps = 0
        visited = set()
        visited.add(target.val)

        while queue:

            for _ in range(len(queue)):

                val = queue.popleft()

                if steps == k:
                    ans.append(val)

                for neighbor in graph[val]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            steps += 1

        return ans
