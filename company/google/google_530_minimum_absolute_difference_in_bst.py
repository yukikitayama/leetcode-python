"""
- Inorder traversal
"""


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        inorder = []

        def dfs(node):
            if node.left:
                dfs(node.left)
            inorder.append(node.val)
            if node.right:
                dfs(node.right)

        dfs(root)

        return min(abs(a - b) for a, b in zip(inorder, inorder[1:]))


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    print(Solution().getMinimumDifference(root))
