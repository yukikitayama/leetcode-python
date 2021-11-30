"""
- Postorder traversal, left, right, root
"""


from typing import Optional, Union


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class NodeValue:
    def __init__(self, min_node, max_node, max_size):
        self.max_node = max_node
        self.min_node = min_node
        self.max_size = max_size


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        return self.largest_bst_subtree_helper(root).max_size
        pass

    def largest_bst_subtree_helper(self, root):
        if not root:
            # min is inf, max is -inf
            return NodeValue(float('inf'), float('-inf'), 0)

        left = self.largest_bst_subtree_helper(root.left)
        right = self.largest_bst_subtree_helper(root.right)

        if left.max_node < root.val < right.min_node:
            return NodeValue(
                min(root.val, left.min_node),
                max(root.val, right.max_node),
                left.max_size + right.max_size + 1
            )

        return NodeValue(float('-inf'), float('inf'), max(left.max_size, right.max_size))


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(1)
root.left.right = TreeNode(8)
root.right.right = TreeNode(7)
print(Solution().largestBSTSubtree(root))

