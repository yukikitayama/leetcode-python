from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')

        def recursion(node, min_, max_):

            nonlocal ans

            if not node:
                return

            min_ = min(node.val, min_)
            max_ = max(node.val, max_)
            v = max_ - min_
            ans = max(ans, v)

            if node.left:
                recursion(node.left, min_, max_)
            if node.right:
                recursion(node.right, min_, max_)

        recursion(root, float('inf'), float('-inf'))

        return ans


if __name__ == '__main__':
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)
    root.right.right = TreeNode(14)
    root.right.right.left = TreeNode(13)
    print(Solution().maxAncestorDiff(root))

