"""
Collect leaves
  DFS to left first
  When it's a left, save current value to array

Left boundary
  dfs to root left child
  append current value to left boundary array
  if left child exists,
    dfs to left
  if not left and right
    dfs to right
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:

        # Edge
        if not root:
            return []

        # Edge
        if root and not root.left and not root.right:
            return [root.val]

        leaves = []

        def collect_leaves(node):

            if node != root and not node.left and not node.right:
                leaves.append(node.val)
                return

            if node.left:
                collect_leaves(node.left)
            if node.right:
                collect_leaves(node.right)

        lefts = []
        rights = []

        def collect_boundaries(node, is_left):

            # Avoid leaves
            if not node.left and not node.right:
                return

            if is_left:
                lefts.append(node.val)
                if node.left:
                    collect_boundaries(node.left, is_left)
                elif not node.left and node.right:
                    collect_boundaries(node.right, is_left)

            else:
                rights.append(node.val)
                if node.right:
                    collect_boundaries(node.right, is_left)
                elif not node.right and node.left:
                    collect_boundaries(node.left, is_left)

        if root.left:
            collect_boundaries(root.left, True)
        collect_leaves(root)
        if root.right:
            collect_boundaries(root.right, False)
            rights.reverse()

        # print([root.val], lefts, leaves, rights)

        return [root.val] + lefts + leaves + rights
