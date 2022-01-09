from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')

        def inorder(node):
            nonlocal prev
            if not node:
                return True

            # Inorder first go to left
            if not inorder(node.left):
                return False

            # Then root
            if node.val <= prev:
                return False

            prev = node.val
            # Finally right
            return inorder(node.right)

        return inorder(root)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, low=float('-inf'), high=float('inf')):

            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return (
                validate(node.left, low, node.val)
                and validate(node.right, node.val, high)
            )

        return validate(root)
