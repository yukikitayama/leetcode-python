"""
Recursion
Optimize, if curr < low, only right. If curr > high, only left
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        ans = 0

        def recursion(node):
            nonlocal ans

            if not node:
                return

            if low <= node.val <= high:
                ans += node.val

            if node.left and node.val >= low:
                recursion(node.left)
            if node.right and node.val <= high:
                recursion(node.right)

        recursion(root)

        return ans


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)
    low = 7
    high = 15
    print(Solution().rangeSumBST(root, low, high))
