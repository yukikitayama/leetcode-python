"""
-
"""


from typing import Optional, Union


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.previous = None

        if self.is_valid_bst(root):
            return self.count_nodes(root)

        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))

    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if not self.is_valid_bst(root.left):
            return False

        # If not increasing order
        if self.previous and self.previous.val >= root.val:
            return False

        self.previous = root

        return self.is_valid_bst(root.right)

    def count_nodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(1)
root.left.right = TreeNode(8)
root.right.right = TreeNode(7)
print(Solution().largestBSTSubtree(root))

