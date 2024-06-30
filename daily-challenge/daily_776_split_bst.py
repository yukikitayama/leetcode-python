from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:

        if not root:
            return [None, None]

        # Current node can be right
        if root.val > target:

            # Left subtree could contain <= target
            left = self.splitBST(root.left, target)

            root.left = left[1]

            return [left[0], root]

        # Current node can be left
        else:

            right = self.splitBST(root.right, target)

            root.right = right[0]

            return [root, right[1]]
