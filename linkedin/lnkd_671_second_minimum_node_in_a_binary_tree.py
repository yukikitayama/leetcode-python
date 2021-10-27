from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        ans = float('inf')
        minimum = root.val

        def dfs(node):
            nonlocal ans
            if node:
                if minimum < node.val < ans:
                    ans = node.val
                elif node.val == minimum:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        return ans if ans != float('inf') else -1


root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
print(Solution().findSecondMinimumValue(root))
