from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_sum = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_gain(root)
        return self.max_sum

    def max_gain(self, node: TreeNode) -> int:
        # No children case. Need this to end recursion
        if not node:
            return 0

        # max(x, 0) because we wanna think whether it's worth it to add
        left_gain = max(self.max_gain(node.left), 0)
        right_gain = max(self.max_gain(node.right), 0)
        new_path = node.val + left_gain + right_gain

        # Check whether we forget about the parent and start a new path
        self.max_sum = max(self.max_sum, new_path)

        # Need this to finish recursion when summed up children
        # max(left_gain, right_gain) because a node appears at most once.
        # You can't sum left and right to node.val when return it to parent
        return node.val + max(left_gain, right_gain)


