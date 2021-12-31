"""
- Recursion
  - max so far
  - min so far
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        def helper(node, cur_max, cur_min):

            if not node:
                return cur_max - cur_min

            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)

            left_max_diff = helper(node.left, cur_max, cur_min)
            right_max_diff = helper(node.right, cur_max, cur_min)

            return max(left_max_diff, right_max_diff)

        return helper(root, root.val, root.val)


if __name__ == '__main__':
    root = TreeNode(8)

