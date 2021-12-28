from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

        def trim(node):

            if not node:
                return None

            # If current node value is too low,
            # in BST, a higher value could exist to the right child
            elif node.val < low:
                return trim(node.right)

            # If current node value is too high,
            # BST could contain lower values to the left child
            # and return the child node to replace the current node if it finds
            elif node.val > high:
                return trim(node.left)

            # Otherwise current node value is in the range,
            # so go to its children and recursively check whether a node value is in range
            # At the end, return the current node for parent.
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)
