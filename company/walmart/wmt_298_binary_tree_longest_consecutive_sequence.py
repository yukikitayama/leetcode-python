"""
dfs(node, parent_num, length)
  if curr num is parent num + 1, update ans
  recursion to left and right
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        ans = 1

        def dfs(node, parent_num, length):
            nonlocal ans

            if node:

                if parent_num is not None and node.val == parent_num + 1:
                    ans = max(ans, length + 1)
                    dfs(node.left, node.val, length + 1)
                    dfs(node.right, node.val, length + 1)

                else:
                    dfs(node.left, node.val, 1)
                    dfs(node.right, node.val, 1)

        dfs(root, None, 1)

        return ans
