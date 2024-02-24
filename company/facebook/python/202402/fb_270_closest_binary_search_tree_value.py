"""
DFS
  in each node compute abs diff
  min so far
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_so_far = float("inf")
        ans = float("inf")

        def recursion(node):
            nonlocal min_so_far, ans

            if node:

                diff = abs(node.val - target)

                if diff < min_so_far:
                    ans = node.val
                    min_so_far = diff
                elif diff == min_so_far and node.val < ans:
                    ans = node.val

                if target < node.val:
                    recursion(node.left)
                elif target > node.val:
                    recursion(node.right)
                # Equal no need to traverse

        recursion(root)

        return ans
