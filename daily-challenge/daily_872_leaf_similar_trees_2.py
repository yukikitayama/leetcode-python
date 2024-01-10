"""
inorder and create leaf value list
compare two lists
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def recursion(node, curr):

            if not node.left and not node.right:
                curr.append(node.val)
                return curr[:]

            if node.left:
                recursion(node.left, curr)
            if node.right:
                recursion(node.right, curr)

            return curr[:]

        leaves_1 = recursion(root1, [])
        leaves_2 = recursion(root2, [])

        return leaves_1 == leaves_2


if __name__ == "__main__":
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.right.left = TreeNode(9)
    root1.right.right = TreeNode(8)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)

    root2 = TreeNode(3)
    root2.left = TreeNode(5)
    root2.right = TreeNode(1)
    root2.left.left = TreeNode(6)
    root2.left.right = TreeNode(7)
    root2.right.left = TreeNode(4)
    root2.right.right = TreeNode(2)
    root2.right.right.left = TreeNode(9)
    root2.right.right.right = TreeNode(8)

    print(Solution().leafSimilar(root1, root2))


