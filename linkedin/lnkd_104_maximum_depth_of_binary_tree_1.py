from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        def dfs(node, depth):
            if not node:
                return

            self.ans = max(self.ans, depth)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 1)

        return self.ans


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().maxDepth(root))
