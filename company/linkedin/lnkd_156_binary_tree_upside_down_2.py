"""
- Go to the deepest leftmost
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Find the deepest leftmost node
        # not root is for the left node in the middle
        # not root.left is for the deepest left node
        if not root or not root.left:
            return root
        new_root = self.upsideDownBinaryTree(root.left)

        # Here root is parent of left
        root.left.left = root.right
        root.left.right = root

        # Current node will be child when making upside down
        # If the current node is in the middle level in the tree,
        # then it needs to update child
        # If the current node is at the top in the tree,
        # then it needs to have none children
        # Current recursion only has current node and children nodes, so
        # the current node children update needs to be done when the current recursion gets out of the stack
        # and updated in the above level in the tree
        root.left = None
        root.right = None
        return new_root


"""
Test


"""




