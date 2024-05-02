from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node, num):
            nonlocal ans

            if node:

                num = num * 10 + node.val

                if not node.left and not node.right:
                    ans += num

                else:
                    dfs(node.left, num)
                    dfs(node.right, num)

        dfs(root, 0)

        return ans