from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        ans = float('-inf')

        def gain_from_subtree(node):

            nonlocal ans

            if not node:
                return 0

            gain_from_left = max(gain_from_subtree(node.left), 0)
            gain_from_right = max(gain_from_subtree(node.right), 0)

            ans = max(ans, gain_from_left + node.val + gain_from_right)

            return max(node.val + gain_from_left, node.val + gain_from_right)

        gain_from_subtree(root)

        return ans
