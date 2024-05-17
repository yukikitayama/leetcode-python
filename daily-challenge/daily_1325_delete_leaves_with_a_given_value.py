"""
DFS
  if current node has target value, and doesn't have children
    return None to its parent
  otherwise return current node (because it's not leaf)
  post order traversal
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def dfs(node):
            if node:

                left = dfs(node.left)
                right = dfs(node.right)

                node.left = left
                node.right = right

                if node.val == target and left is None and right is None:
                    return None

                else:
                    return node

        res = dfs(root)

        return None if res is None else root
