"""
dfs(node, parent, granpa)
  at node, check if granpa is even

dfs(root, None, None)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        ans = 0

        def dfs(node, parent, granpa):
            nonlocal ans

            if node:

                if granpa is not None and granpa.val % 2 == 0:
                    ans += node.val

                dfs(node.left, node, parent)
                dfs(node.right, node, parent)

        dfs(root, None, None)

        return ans
