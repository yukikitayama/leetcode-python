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

            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                dfs(node.left)

            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                dfs(node.right)

        dfs(root)

        queue = collections.deque()
        queue.append(target.val)
        d = 0
        visited = set()
        visited.add(target.val)

        ans = []

        while queue:

            for _ in range(len(queue)):

                curr = queue.popleft()

                if d == k:
                    ans.append(curr)

                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            d += 1

            if d > k:
                break

        return ans