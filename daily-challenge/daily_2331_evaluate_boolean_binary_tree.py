"""
recursion return boolean
  if leaf, return boolean based on value
  if non-leaf, return the results of processing returned value from child
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        def recursion(node):

            if node:

                if not node.left and not node.right:
                    return True if node.val else False

                else:
                    left = recursion(node.left)
                    right = recursion(node.right)

                    if node.val == 2:
                        return left or right
                    elif node.val == 3:
                        return left and right

        return recursion(root)
