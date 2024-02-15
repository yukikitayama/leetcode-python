"""
preorder, root -> left -> right
inplace modify
Head
  Move left child to right child
  Set None for left child
  Next is right child
Middle
  Move left child to right child
  Set parent for left child
  Next is right child
Tail
  Set parent for left child

while loop

Ans
  Recursion returns the tail node of the flattened tree
    This will be left trail for another
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def recursion(node):

            # Terminal: Parent wasn't leaf, but one of its child is None
            if not node:
                return None

            # Terminal: lead
            if not node.left and not node.right:
                return node

            # Post order
            # eg. node: 2, left: 3 (leaf), right: 4 (lead),
            left_tail = recursion(node.left)
            right_tail = recursion(node.right)

            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None

            # Right tail case: Current node right tail will be parent's left tail
            # Left tail case: node: 1, left: 2, right: None, because there is no right, no right tail, so the tail is left tail
            return right_tail if right_tail else left_tail

        recursion(root)