"""
Result
- Start: 5:27
- End: 5:29
- Saw solution: 1
- Solved: 1
- Optimized: 0

Idea
- The given tree is a binary tree, so some part of the tree could not be binary search tree
- But from there, we need to find the binary search tree, and it should be the largest one.
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

        if self.is_valid_bst(root):
            return self.count_nodes(root)

        # If current node is not a root for a valid BST,
        # go to left and right subtrees to find one
        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))

    def find_max(self, root: Optional[TreeNode]) -> Union[int, float]:
        if not root:
            return float('-inf')

        return max(root.val, self.find_max(root.left), self.find_max(root.right))

    def find_min(self, root: Optional[TreeNode]) -> Union[int, float]:
        if not root:
            return float('inf')

        return min(root.val, self.find_min(root.left), self.find_min(root.right))

    def count_nodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
        # Empty tree is a valid binary search tree
        if not root:
            return True

        left_max = self.find_max(root.left)
        if left_max >= root.val:
            return False

        right_min = self.find_min(root.right)
        if right_min <= root.val:
            return False

        # Subtrees also need to be valid BST in order for the current node to be a valid BST
        return self.is_valid_bst(root.left) and self.is_valid_bst(root.right)


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(1)
root.left.right = TreeNode(8)
root.right.right = TreeNode(7)
print(Solution().largestBSTSubtree(root))

