from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]):

        # Returns two elements list
        # first element: Max robbed money starting from the current node and not rob the current node
        # second element: Max robbed money starting from the current node and rob the current node
        def helper(node):
            if not node:
                return 0, 0

            left = helper(node.left)
            right = helper(node.right)

            # If we rob the current node, we cannot rob its children
            rob = node.val + left[1] + right[1]
            # Otherwise, we choose to either rob its children or not
            not_rob = max(left) + max(right)

            return rob, not_rob

        return max(helper(root))
