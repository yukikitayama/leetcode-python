"""
sum of number of edges
  edge between 0 node and nearest non-0 node
BFS from 0?
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def postorder(node):
            nonlocal ans

            if not node:
                return 0

            left = postorder(node.left)
            right = postorder(node.right)

            # Number of exchange
            ans += abs(left) + abs(right)

            # Exchange value
            return node.val - 1 + left + right

        postorder(root)

        return ans
