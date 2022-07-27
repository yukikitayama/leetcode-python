from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:

        def recursion(node):

            if not node:
                return None

            # Leaf
            if not node.left and not node.right:
                return node

            left_tail = recursion(node.left)
            right_tail = recursion(node.right)

            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None

            return right_tail if right_tail else left_tail

        return recursion(root)


