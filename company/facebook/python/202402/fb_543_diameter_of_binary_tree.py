"""
Node wants to sum left length and right legth
  left = recursion
  right = recurion
  update ans if left + right is longer than current ans

  return of recursion is (max length of left or right) + 1

Algo
  Recursion
    max depth of either left or right child
    Leaf
      return 0

    update ans = max(ans, )

    Return
      1 + max(recursion(left child), recursion(right child)
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def recursion(node):
            nonlocal ans

            # Terminal
            if not node:
                return 0

            left_length = recursion(node.left)
            right_length = recursion(node.right)

            ans = max(ans, left_length + right_length)

            return 1 + max(left_length, right_length)

        recursion(root)

        return ans
