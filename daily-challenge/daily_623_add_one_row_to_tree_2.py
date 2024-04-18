"""
Create new tree nodes when current depth is depth - 1
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        # Edge: root is None
        if not root:
            return TreeNode(val)

        # Edge: depth is 1
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node

        def dfs(node, curr_level):

            if node:

                if curr_level == depth - 1:
                    left = node.left
                    insert_left = TreeNode(val)
                    node.left = insert_left
                    insert_left.left = left

                    right = node.right
                    insert_right = TreeNode(val)
                    node.right = insert_right
                    insert_right.right = right

                    return

                else:
                    dfs(node.left, curr_level + 1)
                    dfs(node.right, curr_level + 1)

        dfs(root, 1)

        return root
