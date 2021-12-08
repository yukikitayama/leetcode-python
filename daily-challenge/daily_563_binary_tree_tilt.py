from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def recursion(node):

            nonlocal ans

            if not node:
                return 0

            # Postorder traversal
            left = recursion(node.left)
            right = recursion(node.right)
            tilt = abs(left - right)

            ans += tilt

            return left + node.val + right

        recursion(root)

        return ans


