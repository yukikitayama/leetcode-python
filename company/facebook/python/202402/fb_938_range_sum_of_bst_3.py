from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0

        def recursion(node):
            nonlocal ans

            if node:

                if low <= node.val <= high:
                    ans += node.val

                if node.val > low:
                    recursion(node.left)

                if node.val < high:
                    recursion(node.right)

        recursion(root)

        return ans

    def rangeSumBST1(self, root: Optional[TreeNode], low: int, high: int) -> int:

        ans = 0

        def inorder(node):
            nonlocal ans

            if node:

                inorder(node.left)

                # Terminate early
                if node.val > high:
                    return

                if low <= node.val <= high:
                    ans += node.val

                inorder(node.right)

        inorder(root)

        return ans