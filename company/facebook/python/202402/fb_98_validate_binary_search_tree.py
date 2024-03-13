"""
Preorder
Boolean variable outside recursion
  if current value isn't valid compared to its children's value
    update outside variable to be false
Return the boolean

test case
  5
    L: 4
      L: None
      R: None
    R: 6
      L: 3
      R: 7
exp: F
[4, 5, 3, 6, 7]

Inorder traversal
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid = True
        prev = None

        def inorder(node):
            nonlocal valid, prev
            if node:

                left = inorder(node.left)

                if prev is not None:
                    if prev >= node.val:
                        valid = False

                prev = node.val

                right = inorder(node.right)

        inorder(root)

        return valid

    def isValidBST1(self, root: Optional[TreeNode]) -> bool:

        valid = True

        def recursion(node):
            nonlocal valid
            if node:

                if node.left and node.left.val >= node.val:
                    valid = False

                if node.right and node.right.val <= node.val:
                    valid = False

                recursion(node.left)
                recursion(node.right)

        recursion(root)

        return valid
