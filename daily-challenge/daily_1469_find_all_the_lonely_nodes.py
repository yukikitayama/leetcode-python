"""
recursion(node, lonely flag)
  if leaf and lonely
    append current value
  if has only one child
    lonely flag true
    recursion
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def recursion(node, lonely):
            if node:

                if lonely:
                    ans.append(node.val)

                recursion(node.left, node.right is None)
                recursion(node.right, node.left is None)

        recursion(root, False)

        return ans

    def getLonelyNodes1(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def recursion(node, lonely):
            if node:

                if lonely:
                    ans.append(node.val)

                if (
                    (node.left and not node.right)
                    or (not node.left and node.right)
                ):
                    lonely = True
                else:
                    lonely = False

                recursion(node.left, lonely)
                recursion(node.right, lonely)

        recursion(root, False)

        return ans