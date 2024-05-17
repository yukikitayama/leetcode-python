"""
2 choices
  Rob current
    We can rob if previous was skip
  Skip current
    We can skip regardless of the previous action
"""

from typing import Optional
import functools


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        @functools.cache
        def dp(node, parent_robbed):

            if not node:
                return 0

            # Need to skip current
            if parent_robbed:
                return dp(node.left, False) + dp(node.right, False)

            else:
                rob = node.val + dp(node.left, True) + dp(node.right, True)
                skip = dp(node.left, False) + dp(node.right, False)
                return max(rob, skip)

        return dp(root, False)

    def rob1(self, root: Optional[TreeNode]) -> int:

        # [rob current node, skip current node]
        def recursion(node):
            if not node:
                return [0, 0]

            left = recursion(node.left)
            right = recursion(node.right)

            rob = node.val + left[1] + right[1]

            skip = max(left) + max(right)

            return [rob, skip]

        return max(recursion(root))
