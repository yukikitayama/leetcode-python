"""
- Recursion function returns boolean whether it contains 1
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def recursion(node):

            if not node:
                return False

            is_left_good = recursion(node.left)
            is_right_good = recursion(node.right)

            if not is_left_good:
                node.left = None
            if not is_right_good:
                node.right = None

            return node.val == 1 or is_left_good or is_right_good

        return root if recursion(root) else None

