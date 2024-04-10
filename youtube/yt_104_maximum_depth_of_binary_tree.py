from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def recursion(node, curr_num):
            nonlocal ans

            if node:

                # Left
                if not node.left and not node.right:
                    ans = max(ans, curr_num)

                recursion(node.left, curr_num + 1)
                recursion(node.right, curr_num + 1)

        recursion(root, 1)

        return ans
