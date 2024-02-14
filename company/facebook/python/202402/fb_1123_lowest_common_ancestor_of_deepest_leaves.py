"""
First DFS to assign each node the depth
  hashmap
    k: node
    v: depth
Find max depth from the hashmap
Second DFS

  preorder traversal

If current node is deepest
  Update answer node
  return this node
else
  return none
If current node has both left and right child are deepest
  current node is the answer

"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        depth = {None: -1}

        def dfs1(node, parent=None):
            if node:
                depth[node] = depth[parent] + 1
                dfs1(node.left, node)
                dfs1(node.right, node)

        dfs1(root)

        max_depth = max(depth.values())

        ans = None

        def dfs2(node):
            nonlocal ans

            if not node:
                return None

            if depth[node] == max_depth:
                ans = node
                return node

            left = dfs2(node.left)
            right = dfs2(node.right)

            if left and right:
                ans = node
                return node
            elif left:
                return left
            elif right:
                return right
            else:
                None

        dfs2(root)

        return ans