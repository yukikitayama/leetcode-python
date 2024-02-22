"""
Preorder traversal
Increment answer value with current node valu
if current value < high
  go to right
    if current value > high, righ child has no nodes to meet the condition
if current value > low
  go to left
Terminate if current node is None
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        ans = 0

        def preorder(node):
            nonlocal ans

            if not node:
                return

            if low <= node.val <= high:
                ans += node.val

            if node.val < high:
                preorder(node.right)
            if node.val > low:
                preorder(node.left)

        preorder(root)

        return ans
