"""
DFS
  track max depth so far when reaching leaf
  if difference between max depth so far and current depth is more than 1
    return False
return True
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def recursion(node):
            if not node:
                return True, -1

            is_left_balanced, left_height = recursion(node.left)

            if not is_left_balanced:
                return False, 0

            is_right_balanced, right_height = recursion(node.right)

            if not is_right_balanced:
                return False, 0

            return abs(left_height - right_height) < 2, 1 + max(left_height, right_height)

        return recursion(root)[0]
