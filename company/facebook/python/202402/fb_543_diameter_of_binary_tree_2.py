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

            if node:
                left = recursion(node.left)
                right = recursion(node.right)

                ans = max(ans, left + right)

                return 1 + max(left, right)

            else:
                return 0

        recursion(root)

        return ans
