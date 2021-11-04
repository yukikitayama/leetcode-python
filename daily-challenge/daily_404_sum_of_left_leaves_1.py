"""
- Initialize ans to 0
- recursion preorder traversal by root left right
- if left child is None and right child is None, and left flag is True
  - increment ans
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def preorder(node, left):

            nonlocal ans

            if not node:
                return

            if not node.left and not node.right and left:
                ans += node.val

            preorder(node.left, True)
            preorder(node.right, False)

        preorder(root, False)

        return ans


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# root = TreeNode(1)

print(Solution().sumOfLeftLeaves(root))
