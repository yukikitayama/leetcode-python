"""
- Inorder traversal of Binary Search Tree is a sorted array
"""


from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []

        nums = inorder(root)

        ans = float('inf')

        for i in range(1, len(nums)):

            ans = min(ans, nums[i] - nums[i - 1])

        return ans


if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    print(Solution().minDiffInBST(root))
