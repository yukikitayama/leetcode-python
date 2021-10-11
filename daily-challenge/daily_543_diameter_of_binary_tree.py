"""
- DFS
-
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def longest_path(node):
            if not node:
                return 0

            nonlocal diameter

            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            diameter = max(diameter, left_path + right_path)

            return max(left_path, right_path) + 1

        longest_path(root)

        return diameter



"""
Test
root: [1,2,3,4,5]
    1
   / \
  2   3
 / \
4   5
diameter: 0, longest_path(1)
  node: 1, if1: F, left_path: longest_path(2)
    node: 2, if1: F, left_path: longest_path(4)
      node: 4, if1: F, left_path: longest_path(None_left)
        node: None_left, if1: T, return 0
      left_path: 0, right_path: longest_path(None_right)
        node: None_right, if1: T, return 0
      diameter: max(0, 0 + 0) = 0, return max(left_path, right_path) + 1 = 1
    left_path: 1, right_path: longest_path(5)
      left_path: 0, right_path: 0, diameter: 0, return max(left_path, right_path) + 1 = 1
    diameter: max(diameter, left_path + right_path) = max(0, 2), return max(left_path, right_path) + 1 = 2
"""



