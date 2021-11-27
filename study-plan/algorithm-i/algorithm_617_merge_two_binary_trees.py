"""
- get each head, sum the values, and make a new TreeNode with the value
- go to the left child,
  - left both are not None, do above
  - if either is None, use non None value to make a new TreeNode
  - If both are None, don't make it

Algorithm
- Modify the given root1 input
- Add root2 values to root1 values and return root1
-
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # This covers both returning only root2 value and returning None child because 1 and 2 are both None
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        # If both are not None, sum them
        # Modidy root1 value in place
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1







