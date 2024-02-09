from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
DFS
  terminal
    increment answer by num
  body
    num = num * 10 + curr
"""

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def dfs(node, curr_num):
            nonlocal ans

            curr_num = curr_num * 10 + node.val

            if not node.left and not node.right:
                ans += curr_num
                return

            if node.left:
                dfs(node.left, curr_num)
            if node.right:
                dfs(node.right, curr_num)

        dfs(root, 0)

        return ans


