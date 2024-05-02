from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = True
        prev = float("-inf")

        def inorder(node):
            nonlocal ans, prev

            if node:
                # Left
                inorder(node.left)

                # Root
                if prev is None:
                    prev = node.val
                else:
                    if node.val <= prev:
                        ans = False
                    prev = node.val

                # Right
                inorder(node.right)

        inorder(root)

        return ans

    def isValidBST1(self, root: Optional[TreeNode]) -> bool:

        is_valid = True

        def dfs(node, left_bound, right_bound):
            nonlocal is_valid

            if node:

                if node.val <= left_bound or node.val >= right_bound:
                    is_valid = False

                # dfs(node.left, left_bound, min(right_bound, node.val))
                # dfs(node.right, max(left_bound, node.val), right_bound)
                dfs(node.left, left_bound, node.val)
                dfs(node.right, node.val, right_bound)

        dfs(root, float("-inf"), float("inf"))

        return is_valid