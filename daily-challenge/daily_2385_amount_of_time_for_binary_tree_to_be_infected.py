"""
DFS to create graph
BFS from start
"""

from typing import Optional
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

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

        # print(graph)

        queue = collections.deque()
        queue.append(start)
        ans = -1
        visited = set()
        visited.add(start)

        while queue:

            for _ in range(len(queue)):

                curr = queue.popleft()

                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            ans += 1

        return ans


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(5)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(6)
    root.left.right.left = TreeNode(9)
    root.left.right.right = TreeNode(2)
    start = 3
    print(Solution().amountOfTime(root, start))



