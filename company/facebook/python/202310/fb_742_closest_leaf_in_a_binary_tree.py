"""
- Need to return a leaf node and nearest
- BFS?

- DFS to convert binary tree to graph, where key is TreeNode and value is a list of TreeNodes
  - Each node in graph has at most 3 edges because the graph is made by binary tree
- BFS to start from target node to find the nearest leaf
  - Leaf in the graph has a list less than or equal to 1, because it's leaf, so it only connected to parent
"""


from typing import Optional
import collections
import pprint


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        graph = collections.defaultdict(list)

        def dfs(curr, parent=None):
            if curr:

                graph[curr].append(parent)
                graph[parent].append(curr)
                dfs(curr.left, curr)
                dfs(curr.right, curr)

        dfs(root)

        # for key in graph:
        #     value = graph[key]
        #     if key:
        #         print(f'key: {key.val}')
        #     else:
        #         print(f'key: None')
        #     for v in value:
        #         if v:
        #             print(f'value: {v.val}')
        #         else:
        #             print(f'value: None')

        # BFS
        queue = collections.deque(node for node in graph if node and node.val == k)

        # print(f'queue: {queue}')

        seen = set(list(queue))

        # print(f'seen: {seen}')

        while queue:

            curr = queue.popleft()

            if curr:

                # If curr is leaf
                if len(graph[curr]) == 1:
                    return curr.val

                for neighbor in graph[curr]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    k = 2

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    k = 1

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    root.left.left.left.left = TreeNode(6)
    k = 3
    print(Solution().findClosestLeaf(root, k))
