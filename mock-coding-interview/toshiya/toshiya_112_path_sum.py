from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans = False

        def recursion(node, curr_sum):
            nonlocal ans

            if node:

                # Leaf
                if not node.left and not node.right:
                    if curr_sum + node.val == targetSum:
                        ans = True

                recursion(node.left, curr_sum + node.val)
                recursion(node.right, curr_sum + node.val)

        recursion(root, 0)

        return ans
