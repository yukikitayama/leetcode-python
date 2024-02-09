from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
recursion
  if curr val in range
     add to sum

  if not child
     stop

  if left child, and if curr val > low
     recursive to left
  vice verse
"""


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        ans = 0

        def recursion(node):
            nonlocal ans

            if low <= node.val <= high:
                ans += node.val

            # Terminal for recursion
            if not node.left and not node.right:
                return

            if node.left and node.val > low:
                recursion(node.left)
            if node.right and node.val < high:
                recursion(node.right)

        recursion(root)

        return ans
